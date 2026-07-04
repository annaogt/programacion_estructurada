"""
Crear un proyecto que permita gestionar (administrar) peliculas.
Coloca un menu de opciones:Agregar,Borrar,Modificar,mostrar,buscar ,limpiar una lista de peliculas.

Notas:
1- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2-Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas.
3-Utilizar o implemetar BD relacional con MySQL para guardar infromacion 

"""

import peliculas

opc="1"
pelis=[]
while opc!="7":
    peliculas.borrarPantalla()
    opc=peliculas.menuPrincipal()
    match opc:
        case "1":
               peliculas.borrarPantalla()
               peliculas.agregarPeliculas(pelis)
        case "2":
               peliculas.borrarPantalla()
               peliculas.borrarPeliculas(pelis)
        case "3":
               peliculas.borrarPantalla()
               peliculas.ModificarPeliculas(pelis)
        case "4":
               peliculas.borrarPantalla()
               peliculas.mostrarPeliculas(pelis)
        case "5":
               peliculas.borrarPantalla()
               peliculas.buscarPeliculas(pelis)
        case "6":
               peliculas.borrarPantalla()
               peliculas.limpiarPeliculas(pelis)
        case "7":
               peliculas.borrarPantalla()
               peliculas.terminarSistema()
        case _:
               peliculas.opcionInvalida()