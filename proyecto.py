import sqlite3
#vamoooo
conexion = sqlite3.connect("vivaespana.db")
cursor = conexion.cursor()

cursor.execute(''' INSERT INTO comunidades (id_comunidades,nombre,poblacion) VALUES (?, ?, ?)''', (1,"Andalucía",8733535))

comunidades= [
    (2,"Madrid",3506730),
    (3,"Cataluña",8012231),
    (4,"Murcia",479405)
]
cursor.executemany(''' INSERT INTO comunidades (id_comunidades,nombre,poblacion) VALUES(?, ?, ?)''', comunidades)

conexion.comit()
conexion.close()