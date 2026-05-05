He preparado este pequeño programa para organizar un poco la información de las comunidades, provincias y ciudades. Es algo sencillo, pero espero que funcione bien.
Sobre las tablas y para qué sirven
He intentado que la base de datos (vivaespana.db) sea fácil de entender:
 •	Comunidades: Solo para guardar los nombres de las comunidades y cuánta gente vive en ellas.
 •	Provincias: Para listar las provincias y que cada una sepa a qué comunidad pertenece.
 •	Ciudad: Para los municipios, donde además hemos añadido quién es el alcalde para que esté más completo.
Cómo hacer funcionar el programa
No es muy complicado, solo hay que seguir estos pasos:
 1.	Tener instalado Python (hemos  usado la versión 3).
 2.	Dejar el archivo del código y la base de datos en la misma carpeta, si no, es posible que dé algún fallo al no encontrar los datos.
 3.	Abrir la terminal o el símbolo del sistema y ejecutar el archivo con python nombre_del_archivo.py o con el botón de play.
 4.	Luego solo hay que ir pulsando los números que salen en el menú para moverse por las opciones.
Cómo hemos hecho las funciones (CRUD)
Hemos puesto cuatro opciones básicas en cada tabla:
 1.	Ver datos: Para poder leer lo que hay guardado.
 2.	Añadir: Por si falta alguna información y queremos meterla.
 3.	Actualizar: Por si me he equivocado al escribir algo o algún dato cambia.
 4.	Borrar: Para quitar lo que ya no haga falta. Solo pide el ID para no borrar lo que no debe.
NOTA: He intentado que sea estable, pero si el programa pide un número (como un ID) y se escribe una letra por error, el programa se parará. Lo siento por ese detalle, con tener un poco de cuidado no debe fallar.

