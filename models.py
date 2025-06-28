import sqlite3
from db import get_db

def verify_user(username, password):
    db = get_db()
    cur = db.execute('SELECT * FROM teachers WHERE username = ? AND password = ?', (username, password))
    return cur.fetchone() is not None

def get_all_students():
    db = get_db()
    return db.execute('SELECT * FROM students').fetchall()

def add_or_update_student(name, subject, marks):
    db = get_db()
    cur = db.execute('SELECT * FROM students WHERE name = ? AND subject = ?', (name, subject))
    student = cur.fetchone()
    if student:
        new_marks = student['marks'] + int(marks)
        db.execute('UPDATE students SET marks = ? WHERE id = ?', (new_marks, student['id']))
    else:
        db.execute('INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)', (name, subject, marks))
    db.commit()

def update_student(student_id, marks):
    db = get_db()
    db.execute('UPDATE students SET marks = ? WHERE id = ?', (marks, student_id))
    db.commit()

def delete_student(student_id):
    db = get_db()
    db.execute('DELETE FROM students WHERE id = ?', (student_id,))
    db.commit()
