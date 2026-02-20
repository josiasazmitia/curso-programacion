# Ejercicio 02: Student con más notas

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Luis")
for grade in [70, 85, 95, 88]:
    student.add_grade(grade)

print("Estudiante:", student.name)
print("Notas:", student.grades)
print("Promedio:", round(student.average(), 2))
