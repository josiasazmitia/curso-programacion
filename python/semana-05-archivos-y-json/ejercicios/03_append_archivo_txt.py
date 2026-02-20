# Ejercicio 03: agregar contenido al archivo

archivo = "python/semana-05-archivos-y-json/ejercicios/datos.txt"

with open(archivo, "a", encoding="utf-8") as f:
    f.write("Línea agregada\n")

print("Contenido agregado")
