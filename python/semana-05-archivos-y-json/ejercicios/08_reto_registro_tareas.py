# Ejercicio 08: mini registro de tareas en JSON
import json

archivo = "python/semana-05-archivos-y-json/ejercicios/tareas.json"

def cargar_tareas():
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_tareas(tareas):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


tareas = cargar_tareas()
nueva_tarea = input("Escribe una tarea: ")
tareas.append({"tarea": nueva_tarea, "completada": False})
guardar_tareas(tareas)

print("Tareas guardadas:")
for t in tareas:
    print("-", t["tarea"])
