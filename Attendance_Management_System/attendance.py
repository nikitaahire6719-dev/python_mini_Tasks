from student import Student
from file_manager import write_attendance

class Attendance:
    def mark_present(self, student: Student ):
        write_attendance(student.student_id, student.name, "Present" )
        print("Attendance marked as Present")

    def mark_absent(self, student: Student ):
        write_attendance(student.student_id, student.name, "Absent")
        print("Attendance marked as Absent")

