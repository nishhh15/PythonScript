student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name} marks: {marks}")
else:
    print("Student not found")