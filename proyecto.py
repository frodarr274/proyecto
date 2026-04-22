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

conexion = sqlite3.connect("proyecto.db")
cursor=conexion.cursor()
try:
    cursor.execute(''' INSERT INTO comunidad (nombre, provincia, poblacion) VALUES (?,?,?)''')

    comunidad = [



    ]

    cursor.executemany(''' INSERT INTO comunidad (nombre, provincia, poblacion) VALUES (?,?,?)''' ,provincia)

    cursor.execute('''SELECT * FROM comunidad''')
   resultados= cursor.fetchall()

    for fila in resultados:
    print (fila)


    cursor.execute('''UPDATE comunidad SET poblacion = ? WHERE nombre = ? ''')
                                                                                            

    cursor.execute(''' DELETE FROM comunidad WHERE nombre = ?''')

    conexion.commit()
except Excepcion as e:
    print ("Ha ocurrido un error con los datos selecionados", e)
    conexion.rollback()
finally:
    conexion.close()                                                                                        







