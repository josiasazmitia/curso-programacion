# Ejercicio 07: funciones con colecciones

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


notas_estudiante = [80, 75, 90, 88]
print("Promedio:", calcular_promedio(notas_estudiante))
