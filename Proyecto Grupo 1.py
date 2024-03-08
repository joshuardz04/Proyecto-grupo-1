tareas = {}

def agregar_tarea():
    nombre = input("¿Que tarea desea hacer?: ")
    tareas[nombre] = False

def editar_tarea():
    nombre = input("Ingrese el nombre de la tarea que quiere editar: ")
    if nombre in tareas:
        tareas[nombre] = not tareas[nombre]
    else:
        print("Tarea no existe.")

def borrar_tarea():
    nombre = input("Ingrese el nombre de la tarea que quiere borrar: ")
    if nombre in tareas:
        del tareas[nombre]
    else:
        print("Tarea no existe.")

def ver_tareas():
    for nombre, completada in tareas.items():
        print(f"{nombre}: {'' if completada else '(pendiente)'}" if completada else f"{nombre}: (pendiente)")

def marcar_completada():
    nombre = input("Tarea que desea marcar como completada: ")
    if nombre in tareas:
        tareas[nombre] = True
    else:
        print("Tarea no existe.")

while True:
    print("\nSeleccione una opcion:")
    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Borrar tarea")
    print("4. Ver tareas")
    print("5. Marcar tarea como completada")
    print("6. Salir")
    opcion = int(input("Ingrese el numero de la opcion que desea: "))
    if opcion == 1:
        agregar_tarea()
    if opcion == 2:
        editar_tarea()
    if opcion == 3:
        borrar_tarea()
    if opcion == 4:
        ver_tareas()
    if opcion == 5:
        marcar_completada()
    if opcion == 6:
        break
    else:
        print("Error.")