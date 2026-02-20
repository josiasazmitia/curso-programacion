# Ejercicio 01: leer archivo txt

archivo = "python/semana-05-archivos-y-json/ejercicios/nota.txt"

# Crea una nota base para evitar error en la primera ejecución
with open(archivo, "w", encoding="utf-8") as f:
    f.write("Primer mensaje de prueba\n")

with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)
