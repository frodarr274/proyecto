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






