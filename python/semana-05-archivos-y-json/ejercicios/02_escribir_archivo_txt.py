# Ejercicio 02: escribir archivo txt

archivo = "python/semana-05-archivos-y-json/ejercicios/datos.txt"

with open(archivo, "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")

print("Archivo escrito correctamente")
