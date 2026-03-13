conexion sqlite3.connect("proyecto.db")
cursor=conexion.cursor()
cursor execute('''
INSERT INTO España(provincia,comida,id_identificación) VALUES (sevilla, pescaito,1)''')