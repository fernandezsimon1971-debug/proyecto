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

# Clase sistema de gestion de tareas

class SistemaGestionTareas:
    #Inicializacion del sistema de gestión de un archivo
    def __init__(self, archivo_datos = "datos_usuarios.json"):
        self.usuarios = {}
        self.archivos_datos = archivo_datos
        self.cargar_datos()

    def cargar_datos(self):
        #Cargar datos de los usuarios en json
        try:
            with open(self.archivos_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    #crea un objeto usuario para cada usuario en los datos
                    usuario = usuario(nombre_usuario, info["contrasena"])
                    for tarea_info in info ["tareas"]:
                        # Crea un objeto tareas para cada tarea de usuario
                        tarea = tarea(tarea_info["titulo"], tarea_info["descripcion"], tarea_info["fecha_vencimiento"])
                        tarea.completado = tarea_info["completada"]
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError: # Manejo de excepciones
            print("Archivo de datos no encontrado, se creará uno nuevo al guardar")

    def guardar_datos(self):
        # Guardar los datos de los usuarios en el archivo
        datos = {} # este es el diccionario de datos
        for nombre_usuario, usuario in self.usuario.items():
            # Organiza las tareas y la informacion del usuario en un diccionario
            datos[nombre_usuario] = {
                "contrasena": usuario.contrasena,
                "tareas": [
                    {"titulo": tarea.titulo, "descripcion": tarea.descripcion, "fecha_vencimiento": tarea.fecha_vencimiento, "completado": tarea.completada}
                    for tarea in usuario.tareas
                ]
            }
        with open(self.archivos_datos, "w") as archivo:
            json.dump(datos, archivo)

    def registrar_usuario(self, nombre_usuario, contrasena):
        # Registrar un nuevo usuario si el nombre de usuario no existe
        if nombre_usuario in self.usuarios:
            print("El nombre de usuario ya existe")
            return False
        else:
            self.usuarios[nombre_usuario] = usuario(nombre_usuario, contrasena)
            self.guardar_datos()
            print("usuario registrado con exito")
            return True

    def iniciar_sesion(self, nombre_usuario, contrasena):
        #Inicia sesion si el usuario y contrasena coinciden
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.contrasena == contrasena:
            print("Inicio de sesion exitoso")
            return usuario
        else:
            print("Nombre de usuario o contrasena incorrecto")
            return None

    def menu_usuario(self, usuario):
        while True:
            print("\n1. Crear tareas")
            print("2. ver tareas")
            print("3. editar tareas")
            print("4. completar tareas")
            print("5. eliminar tareas")
            print("6. Cerrar sesion")

        opcion = input("Slecciona una opcion: ")

        if opcion == "1":
            titulo = input("Titulo de la tarea: ")
            descripcion = input("Ingresa la descripcion: ")
            fecha_vencimiento = input("Fech de vencimiento (YYY-MM-DD):  ")
            tarea = tarea(titulo, descripcion, fecha_vencimiento)
            usuario.agregar_tarea(tarea)
            self.guardar_datos()
            print("Tarea creada con éxito")

        elif opcion =="2":
            tareas = usuarios.obtener_tareas()
            if not tareas:
                print("No tiene tareas")
            for idx, tarea in enumerate(tarea, start=1):
                estado = "completado" if tarea.completado else "Pendiente"
                print(f"{idx}. {tarea.titulo} {estado} (vence: {tarea.fecha_vencimiento})")

        elif opcion == "3":
            titulo_tarea = input("titulo de la tarea a editar: ")
            tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)
            if tarea:
                nuevo_titulo = input("Nuevo titulo: ")
                nueva_descripcion = input("Nueva descripcion: ")
                nueva_fecha = input("Nueva fecha de vencimiento: ")
                tarea.editar_tarea(nuevo_titulo, nueva_descripcion, nueva_fecha)
                self.guardar_datos()
                print("Tarea actualizada con éxito")
            else:
                print("Tarea no encontrada")

        elif opcion == "4":
            # Marcar una tarea como completada
            titulo_tarea = input("Titulo de la tarea a completar: ")
            tarea = next((t for t in usuario.tareas if t.titulo == titulo_tareas), None)
            if tarea:
                tarea.marcar_completada()
                self.guardar_datos()
                print("Tarea marcada como completada")
            else:
                print("Tarea no encontrada")

        elif opcion == "5":
            # Eliminar una tarea
            titulo_tarea = input("Titulo de la tarea a eliminar: ")
            usuario.eliminar_tarea(titulo_tarea)
            self.guardar_datos()
            print("Tarea eliminada con éxito")
        
        elif opcion == "6":
            # Cerrar sesion
            print("Cerrando sesion...")
            break
        else:
            print("opcion no valido, intentalo de nuevo")

# Ejecucion del sistema

if __name__ == "__main__":
    sistema = SistemaGestionTareas()
    print("\n---- Sistema de Gestion de Tareas----")
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    print("3. Salir")
    opcion = input("Seleccionar una opcion: ")

    if opcion == "1":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingresa la contrasena: ")
        sistema.registrar_usuario(nombre_usuario, contrasena)

    elif opcion == "2":
        nombre_usuario = input("Nombre de usuario: ")
        contrasena = input("Contrasena: ")
        usuario = sistema.iniciar_sesion(nombre_usuario, contrasena)
        if usuario:
            sistema.menu_usuario(usuario)

    elif opcion == "3":
        print("saliendo del sistema...")
        break
    else:
        print("opcion no valida, Inténtalo de nuevo")







