"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

alumno = {
    "nombre": "Paty",
    "edad": 17,
    "carrera": "TI"
}

print(alumno)

#Agregar un atributo a un objeto
alumno["correo"] = "paty@utd.edu.mx"

print("Agregar atributo:")
print(alumno)


#Modificar un valor de un item o atributo que ya existe
alumno["edad"] = 18

print("Modificar atributo:")
print(alumno)

#Quitar el ultimo atributo de un objeto 
alumno.popitem()

print("Eliminar último atributo:")
print(alumno)


#Quitar un atributo en especifico de un objeto 
alumno.pop("carrera")

print("Eliminar atributo específico:")
print(alumno)