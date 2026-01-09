FILE_NAME = "student.py"

def read_students():
    students = []
    try:
        with open("student.py", "r") as file:
            for line in file:
                roll, name, age, course = line.strip().split(",")
                students.append([roll, name, int(age), course])
    except FileNotFoundError:
        pass
    return students


def write_students(students):
    with open("student.py", "w") as file:
        for s in students:
            file.write(f"{s[0]},{s[1]},{s[2]},{s[3]}\n")
