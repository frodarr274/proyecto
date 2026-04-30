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
 #seguir con las provincias

  