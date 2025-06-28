DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    marks INTEGER NOT NULL
);

-- Insert a default teacher account
INSERT INTO teachers (username, password) VALUES ('teacher1', 'pass123');
