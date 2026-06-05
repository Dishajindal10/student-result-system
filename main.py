from database import initialize_db
from operations import add_student, add_result, search_student, delete_student, show_all_students
from reports import show_toppers, show_failed_students

def menu():
    initialize_db()
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. Add Result")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Show All Students")
        print("6. Show Top Performers")
        print("7. Show Failed Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            dept = input("Enter department: ")
            add_student(name, roll, dept)
        elif choice == "2":
            roll = input("Enter roll number: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            add_result(roll, subject, marks)
        elif choice == "3":
            roll = input("Enter roll number: ")
            search_student(roll)
        elif choice == "4":
            roll = input("Enter roll number: ")
            delete_student(roll)
        elif choice == "5":
            show_all_students()
        elif choice == "6":
            show_toppers()
        elif choice == "7":
            show_failed_students()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()