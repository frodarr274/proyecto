#Menú del sistema 
import sqlite3
def menu ():
    print("----MENÚ----")
    print("1.Crear")
    print("2.Leer")
    print("3.Actualizar")
    print("4.Borrar")
    print("--------------------------------")
    int(input("Escribe lo que quieres hacer:"))
    continuar=input("¿Quieres hacer algo más?")

    if continuar=="no":
        print ("Adios")
        break
    while menu !="no"

#Para insertar datos
conexion = sqlite3.connect("proyecto.db")
cursor=conexion.cursor()
try:
    cursor.execute(''' INSERT INTO comunidades (id_comunidad,nombre,poblacion) VALUES (?,?,?)''' (1,"Andalucía",125000))

    comunidades = [
        (2,"Madrid", 20000),
        (3,"Extremadura",45000),
        (4,"Galicia", 90000)
    ]

    cursor.executemany(''' INSERT INTO comunidades (id_comunidad,nombre,poblacion) VALUES (?,?,?)''' ,comunidades)

    cursor.execute(''' INSERT INTO provincias (id_provincia,nombre,id_comunidad VALUES (?,?,?)''' (1,"Sevilla",1))

    provincias=[


    ]

    cursor.executemany(''' INSERT INTO provincias (id_provincia,nombre,id_comunidad) VALUES (?,?,?)''' ,provincias)

    cursor.execute(''' INSERT INTO ciudad (id_ciudad,nombre,id_provincia,alcalde) VALUES (?,?,?)''')

    ciudad= [


    ]
    cursor.executemany(''' INSERT INTO ciudad (id_ciudad,nombre,id_provincia,alcalde) VALUES (?,?,?)''' ,ciudad)
    #Para selecionar datos 
    cursor.execute('''SELECT * FROM comunidades''')
   resultados= cursor.fetchall()

    for fila in resultados:
    print (fila)

    #Para borrar o actualizar datos

    cursor.execute('''UPDATE comunidades SET poblacion = ? WHERE nombre = ? ''')
                                                                                            

    cursor.execute(''' DELETE FROM comunidades WHERE nombre = ?''')

    conexion.commit()
    #Para realizar transacciones (se requeria de esto una vez que los datos esten ordenados y los comandos funcionen perfectamente)
except Excepcion as e:
    print ("Ha ocurrido un error con los datos que usted ha seleccionado", e)
    conexion.rollback()
finally:
    conexion.close()                                                                                        







