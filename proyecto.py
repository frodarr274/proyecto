#hay que hacerlo con funcioness
import sqlite3
print("Buenos días, bienvenido a tu tabla.Elige 1 para modificar algo en una de las tablas; 2, para ver algo en una de las tablas; 3 , para actualizar una tabla; 4,para borrar algo de las tablas")
def create(ciudad,comunidades,provincias):#los parámetros son los nombres de lass tablas o los parámetros de esas tablas????
#que tabla quieres modificar(ciudad , comunidades o provincias)
#elige que quieres hacer con la tabla que has elegido(CREATE,READ,UPDATE O DELETE)
#CREO que hay que poner ifs . por ejemplo , si elijo 1,crea ; 2,lee; 3,actualiza; 4 ,borra
    conexion = sqlite3.connect("vivaespana.db")
    

    cursor = conexion.cursor()

    cursor.execute(''' INSERT INTO comunidades (id_comunidad,nombre,poblacion) VALUES (?, ?, ?)''', (1,"Andalucía",8733535))

    comunidades= [
        (2,"Madrid",3506730),
        (3,"Cataluña",8012231),
        (4,"Murcia",479405)
    ]
    cursor.executemany(''' INSERT INTO comunidades (id_comunidad,nombre,poblacion) VALUES(?, ?, ?)''', comunidades)

    conexion.commit()
    conexion.close()

    cursor.execute(''' INSERT INTO provincias (id_provincia,nombre,id_comunidad) VALUES (?, ?, ?)''', (1,"Sevilla",1))

    provincias= [
        (2,"Valencia",1)
        (3,"Barcelona",3)
        (4,"Tarragona",3)
        (5,"Murcia",4)
        (6,"Madrid",2)
    ]
    cursor.executemany(''' INSERT INTO provincias (id_provincia,nombre,id_comunidad) VALUES(?, ?, ?)''', provincias)

    conexion.commit()
    conexion.close()

    cursor.execute (''' INSERT INTO ciudad (id_ciudad,nombre,id_provincia,alcalde) VALUES (?, ?, ?)''',(1,"Dos Hermanas",1,"Francisco Rodriguez"))

    ciudad=[
        (2,"Aledo",5,"Jose Ballesta")
        (3,"Gandía",2,"María José Catala")
        (4,"Alcobendas",6,"Jose Luis Martinez")
    ]
    cursor.executemany(''' INSERT INTO ciudad (id_ciudad,nombre,id_provincia,alcalde) VALUES(?, ?, ?)''', ciudad)

    conexion.commit()
    conexion.close()
                                                                                            







