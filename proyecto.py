import json
from datetime import datetime

#Class Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False # hasta que nosotros no le demos una indicacion de que ya esta completado, debe mantenerse en Falso (sin completar)

    def marcar_completada(self):
        self.completado = True

    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha

class usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tareas = []

    def agregar_tareas(self, tarea):
        self.tarea.append(tarea)

    def eliminar_tarea(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]
        # recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al egresado.
    
    def Obtener_tareas(self):
        return self.tareas


