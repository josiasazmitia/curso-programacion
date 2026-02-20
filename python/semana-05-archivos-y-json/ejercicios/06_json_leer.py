# Ejercicio 06: leer JSON
import json

archivo = "python/semana-05-archivos-y-json/ejercicios/usuarios.json"

with open(archivo, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

for usuario in usuarios:
    print(usuario["nombre"], "-", usuario["edad"])
