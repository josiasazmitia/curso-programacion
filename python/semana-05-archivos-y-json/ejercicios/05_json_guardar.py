# Ejercicio 05: guardar JSON
import json

archivo = "python/semana-05-archivos-y-json/ejercicios/usuarios.json"
usuarios = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 30},
]

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(usuarios, f, ensure_ascii=False, indent=2)

print("JSON guardado")
