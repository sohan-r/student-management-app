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

    # Check if student with same name and subject exists
    existing = conn.execute(
        "SELECT * FROM students WHERE name = ? AND subject = ?",
        (name, subject)
    ).fetchone()

    if existing:
        # Add new marks to existing marks
        updated_marks = existing['marks'] + marks
        conn.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (updated_marks, existing['id'])
        )
    else:
        # Insert new record
        conn.execute(
            "INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)",
            (name, subject, marks)
        )

    conn.commit()
    conn.close()
    return redirect('/home')



@app.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    name = request.form['name']
    subject = request.form['subject']
    new_marks = int(request.form['marks'])

    conn = get_db_connection()

    # Get current record's marks
    current = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    if not current:
        conn.close()
        return redirect('/home')

    # Check for existing record with same name+subject but different ID
    existing = conn.execute('''
        SELECT * FROM students 
        WHERE name = ? AND subject = ? AND id != ?
    ''', (name, subject, id)).fetchone()

    if existing:
        # Combine marks from current and existing records
        total_marks = existing['marks'] + new_marks
        conn.execute('UPDATE students SET marks = ? WHERE id = ?', (total_marks, existing['id']))
        # Delete the current record
        conn.execute('DELETE FROM students WHERE id = ?', (id,))
    else:
        # Update the current record normally
        conn.execute('''
            UPDATE students
            SET name = ?, subject = ?, marks = ?
            WHERE id = ?
        ''', (name, subject, new_marks, id))

    conn.commit()
    conn.close()
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