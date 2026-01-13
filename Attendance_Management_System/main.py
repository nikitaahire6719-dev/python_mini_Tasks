from student import Student
from attendance import Attendance
from file_manager import initialize_file, read_attendance

def main():
    initialize_file()
    attendance = Attendance()

    while True:
        print("\n=== Attendance Management System ===")
        print("1. Mark Present")
        print("2. Mark Absent")
        print("3. View Attendence")
        print("4. Exit")

        choice = input("Enter choice: ")
        
        match choice:
            case "1":
                sid = input("Enter Student ID: ")
                name = input("Enter Name: ")
                student = Student(sid, name)
                attendance.mark_present(student)

            case "2":
                sid = input("Enter Student ID: ")
                name = input("Enter Name: ")
                student = Student(sid , name)
                attendance.mark_absent(student)

            case "3":
                print("\n---- Attendance Records ----")
                print(read_attendance())

            case "4":
                print("Exiting System.")
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
