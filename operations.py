import sqlite3
from database import connect
from models import Student, Result

def add_student(name, roll_number, department):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, roll_number, department) VALUES (?, ?, ?)",
            (name, roll_number, department)
        )
        conn.commit()
        print(f"Student {name} added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Roll number already exists!")
    finally:
        conn.close()

def add_result(roll_number, subject, marks):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM students WHERE roll_number = ?", (roll_number,))
    student = cursor.fetchone()
    if not student:
        print("Error: Student not found!")
        conn.close()
        return
    result = Result(student[0], subject, marks)
    cursor.execute(
        "INSERT INTO results (student_id, subject, marks, grade) VALUES (?, ?, ?, ?)",
        (result.student_id, result.subject, result.marks, result.grade)
    )
    conn.commit()
    print(f"Result added! Grade: {result.grade}")
    conn.close()

def search_student(roll_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    student = cursor.fetchone()
    if not student:
        print("Student not found!")
        conn.close()
        return
    print(f"\nName: {student[1]} | Roll No: {student[2]} | Dept: {student[3]}")
    cursor.execute("SELECT subject, marks, grade FROM results WHERE student_id = ?", (student[0],))
    results = cursor.fetchall()
    if results:
        print("Results:")
        for r in results:
            print(f"  {r[0]}: {r[1]} marks | Grade: {r[2]}")
    else:
        print("No results found.")
    conn.close()

def delete_student(roll_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll_number,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Student not found!")
    else:
        print("Student deleted successfully!")
    conn.close()

def show_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(f"Name: {s[1]} | Roll No: {s[2]} | Dept: {s[3]}")
    conn.close()