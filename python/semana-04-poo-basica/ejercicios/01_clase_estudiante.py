# Ejercicio 01: clase Student básica

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        # Agrega una nota a la lista
        self.grades.append(grade)

    def average(self):
        # Retorna 0 si no hay notas
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Ana")
student.add_grade(80)
student.add_grade(90)
print("Promedio:", student.average())
