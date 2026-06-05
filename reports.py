from database import connect

def show_toppers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT students.name, students.roll_number, AVG(results.marks) as avg_marks
        FROM students
        JOIN results ON students.id = results.student_id
        GROUP BY students.id
        ORDER BY avg_marks DESC
    ''')
    rows = cursor.fetchall()
    print("\n--- Top Performers ---")
    for r in rows:
        print(f"{r[0]} | Roll: {r[1]} | Average Marks: {r[2]:.2f}")
    conn.close()

def show_failed_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT DISTINCT students.name, students.roll_number
        FROM students
        JOIN results ON students.id = results.student_id
        WHERE results.grade = "F"
    ''')
    rows = cursor.fetchall()
    print("\n--- Failed Students ---")
    if not rows:
        print("No failed students!")
    else:
        for r in rows:
            print(f"{r[0]} | Roll: {r[1]}")
    conn.close()