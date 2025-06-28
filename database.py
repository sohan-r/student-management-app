import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    # Create teachers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create students table
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    ''')

    # Insert default teacher if not exists
    c.execute("SELECT * FROM teachers WHERE username = 'admin'")
    if not c.fetchone():
        c.execute("INSERT INTO teachers (username, password) VALUES (?, ?)", ('admin', 'admin123'))
        print("Inserted default teacher credentials: admin / admin123")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
