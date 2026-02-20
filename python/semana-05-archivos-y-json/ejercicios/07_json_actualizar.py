# Ejercicio 07: actualizar JSON
import json

archivo = "python/semana-05-archivos-y-json/ejercicios/usuarios.json"

with open(archivo, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

usuarios.append({"nombre": "Carmen", "edad": 27})

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(usuarios, f, ensure_ascii=False, indent=2)

print("JSON actualizado")
