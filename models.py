class Student:
    def __init__(self, name, roll_number, department):
        self.name = name
        self.roll_number = roll_number
        self.department = department

    def __str__(self):
        return f"Student: {self.name} | Roll No: {self.roll_number} | Dept: {self.department}"


class Result:
    def __init__(self, student_id, subject, marks):
        self.student_id = student_id
        self.subject = subject
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"Subject: {self.subject} | Marks: {self.marks} | Grade: {self.grade}"