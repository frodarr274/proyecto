import sqlite3

# Usamos una clase para agrupar todo el proyecto
class SistemaGeograficoEspaña:
    
    # El Constructor para guardar el nombre de nuestra base de datos
    def __init__(self, nombre_base_datos):
        self.nombre_base_datos = nombre_base_datos

    # Función para abrir la conexión
    def abrir_conexion(self):
        return sqlite3.connect(self.nombre_base_datos)

    # ---  COMUNIDADES  ---
    def gestionar_comunidades(self):
        repetir_comunidades = True
        while repetir_comunidades:
            print("--- MENÚ COMUNIDADES AUTÓNOMAS ---")
            print("1. Ver todas las comunidades")
            print("2. Añadir nueva comunidad")
            print("3. Actualizar comunidad")
            print("4. Borrar comunidad") #  he añadido esto
            print("5. Volver al inicio")
            
            opcion_elegida = input("¿Qué quieres hacer?: ")

            if opcion_elegida == '1':
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM comunidades")# el * es "todos los campos"
                lista_comunidades = cursor.fetchall()
                for fila in lista_comunidades:
                    print(fila)
                conexion.close()

            elif opcion_elegida == '2':
                nombre_comunidad = input("Nombre de la comunidad: ")
                habitantes = int(input("Número de habitantes: "))
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO comunidades (nombre, poblacion) VALUES (?, ?)", 
                               (nombre_comunidad, habitantes))
                conexion.commit()
                conexion.close()
                print("Comunidad guardada.")

            elif opcion_elegida == '3':
                id_modificar = int(input("ID de la comunidad a modificar: "))
                nombre = input("Nuevo nombre: ")
                poblacion = int(input("Nueva población: "))
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("UPDATE comunidades SET nombre = ?, poblacion = ? WHERE id = ?", (nombre, poblacion, id_modificar))
                conexion.commit()
                conexion.close()
                print("Actualizado.")

            elif opcion_elegida == '4': # Lógica de Borrado
                id_borrar = int(input("Introduce el ID de la comunidad que quieres ELIMINAR: "))
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM comunidades WHERE id = ?", (id_borrar,))
                conexion.commit()
                conexion.close()
                print("Comunidad eliminada.")

            elif opcion_elegida == '5':
                repetir_comunidades = False
 
 # --- SECCIÓN DE PROVINCIAS ---
    def gestionar_provincias(self):
        repetir_provincias = True
        while repetir_provincias:
            print("--- MENÚ PROVINCIAS ---")
            print("1. Ver todas las provincias")
            print("2. Añadir nueva provincia")
            print("3. Actualizar provincia")
            print("4. Borrar provincia")
            print("5. Volver")
            
            opcion_elegida = input("Elija opción: ")

            if opcion_elegida == '1':
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM provincias")
                lista_provincias = cursor.fetchall()
                for fila in lista_provincias:
                    print(fila)
                conexion.close()

            elif opcion_elegida == '2':
                nombre_provincia = input("Nombre de la provincia: ")
                id_comunidad_padre = int(input("ID de la comunidad a la que pertenece: "))
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO provincias (nombre, id_comunidad) VALUES (?, ?)", 
                               (nombre_provincia, id_comunidad_padre))
                conexion.commit()
                conexion.close()

            elif opcion_elegida == '3':
                id_modificar = int(input("ID de la provincia a modificar: "))
                nombre = input("Nuevo nombre: ")
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("UPDATE provincias SET nombre = ? WHERE id = ?", (nombre, id_modificar))
                conexion.commit()
                conexion.close()

            elif opcion_elegida == '4':
                id_borrar = int(input("ID de la provincia a eliminar: "))
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM provincias WHERE id = ?", (id_borrar,))
                conexion.commit()
                conexion.close()
                print("Provincia borrada.")

            elif opcion_elegida == '5':
                repetir_provincias = False
 
   # --- SECCIÓN DE CIUDADES---
    def gestionar_ciudades(self):
        repetir_ciudades = True
        while repetir_ciudades:
            print("--- MENÚ CIUDADES ---")
            print("1. Ver ciudades")
            print("2. Añadir ciudad")
            print("3. Volver")
            
            opcion_elegida = input("Elija: ")

            if opcion_elegida == '1':
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM ciudad")
                lista_ciudades = cursor.fetchall()
                for fila in lista_ciudades:
                    print(fila)
                conexion.close()

            elif opcion_elegida == '2':
                nombre_ciudad = input("Nombre de la ciudad: ")
                id_provincia_padre = int(input("ID de la provincia a la que pertenece: "))
                alcalde = input("Nombre del alcalde: ")
                
                conexion = self.abrir_conexion()
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ciudad (nombre, id_provincia, alcalde) VALUES (?, ?, ?)", 
                               (nombre_ciudad, id_provincia_padre, alcalde))
                conexion.commit()
                conexion.close()

            elif opcion_elegida == '3':
                repetir_ciudades = False

#esto es el menú principal

def iniciar_todo():

    # Creamos el objeto principal 
    app = SistemaGeograficoEspaña('vivaespana.db')
    
    ejecutar = True
    while ejecutar:
        print("===============================")
        print(" GESTOR DE GEOGRAFÍA DE ESPAÑA")
        print("===============================")
        print("1. COMUNIDADES")
        print("2. PROVINCIAS")
        print("3. CIUDADES")
        print("4. SALIR")
        
        opcion_menu = input("¿Con qué tabla quieres trabajar?: ")

        if opcion_menu == '1':
            app.gestionar_comunidades()
        elif opcion_menu == '2':
            app.gestionar_provincias()
        elif opcion_menu == '3':
            app.gestionar_ciudades()
        elif opcion_menu == '4':
            print("Saliendo del programa... ¡Adiós!")
            ejecutar = False

if __name__ == "__main__":
    iniciar_todo()                     








                                