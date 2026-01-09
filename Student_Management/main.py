from student import Student
from filehandler import read_students, write_students

students = read_students()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            roll = input("Roll No: ")
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")

            for s in students:
                if s[0] == roll:
                    print("Student already exists")
                    break
            else:
                students.append([roll, name, age, course])
                write_students(students)
                print("Student added")

        case "2":
            if not students:
                print("No students found")
            for s in students:
                print(f"Roll:{s[0]} Name:{s[1]} Age:{s[2]} Course:{s[3]}")

        case "3":
            roll = input("Roll No to update: ")
            for s in students:
                if s[0] == roll:
                    s[2] = int(input("New Age: "))
                    s[3] = input("New Course: ")
                    write_students(students)
                    print("Student updated")
                    break
            else:
                print("Student not found")

        case "4":
            roll = input("Roll No to delete: ")
            for s in students:
                if s[0] == roll:
                    students.remove(s)
                    write_students(students)
                    print("Student deleted")
                    break
            else:
                print("Student not found")

        case "5":
            print("Exiting system")
            break

        case _:
            print("Invalid choice")
