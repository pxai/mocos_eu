import tareas
misTareas = tareas.Tareas()

print(misTareas.mostrar(), "\n---")

misTareas.crear(2, "Eskatzak")
print(misTareas.mostrar(), "\n---")

misTareas.eliminar(2)
print(misTareas.mostrar(), "\n---")

misTareas.crear(66, "Irakurri")
print(misTareas.mostrar(), "\n---")
misTareas.guardar()