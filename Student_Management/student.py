class Student:
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    def to_file(self):
        return f"{self.roll},{self.name},{self.age},{self.course}\n"
