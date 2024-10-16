from Exercise2 import Student
students = []
for _ in range(2):
    stud_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter student course: ")
    mark = float(input("Enter student mark: "))

    student = Student(stud_id, name, course, mark)
    students.append(student)

for student in students:
    print(student)

