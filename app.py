from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret123'

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username, password)).fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('home.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    subject = request.form['subject']
    marks = int(request.form['marks'])
    conn = get_db_connection()
    existing = conn.execute("SELECT * FROM students WHERE name=? AND subject=?", (name, subject)).fetchone()
    if existing:
        conn.execute("UPDATE students SET marks = marks + ? WHERE name=? AND subject=?", (marks, name, subject))
    else:
        conn.execute("INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)", (name, subject, marks))
    conn.commit()
    conn.close()
    return redirect('/home')

@app.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    # Placeholder for edit logic
    return redirect('/home')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/home')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)