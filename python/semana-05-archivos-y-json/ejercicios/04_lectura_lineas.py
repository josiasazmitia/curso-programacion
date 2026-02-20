# Ejercicio 04: lectura por líneas

archivo = "python/semana-05-archivos-y-json/ejercicios/datos.txt"

with open(archivo, "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        print(f"{numero}: {linea.strip()}")
