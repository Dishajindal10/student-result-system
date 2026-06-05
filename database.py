import sqlite3

def connect():
    conn = sqlite3.connect("student_results.db")
    return conn

def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")