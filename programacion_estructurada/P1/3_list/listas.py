import os

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido


numeros = [10, 20, 30, 40, 50]

print("Lista de números:")
print(numeros)

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras = ["hola", "python", "lista", "programacion", "codigo"]

buscar = input("Ingresa una palabra a buscar: ")

if buscar in palabras:
    print("La palabra sí existe en la lista")
else:
    print("La palabra no existe en la lista")


# 2DA FORMA

for palabra in palabras:
    if palabra == buscar:
        print("Palabra encontrada:", palabra)
 

#3er FORMA

print(palabras.count(buscar))

#Ejemplo 3 Añadir elementos a la lista

frutas = ["manzana", "pera", "uva"]

frutas.append("sandia")
frutas.append("melon")

print("Lista de frutas:")
print(frutas)
  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda = [
    ["Paty", "6181234567"],
    ["Luis", "6189876543"],
    ["Ana", "6184567890"]
]

print("Agenda Telefónica")

for persona in agenda:
    print("Nombre:", persona[0])
    print("Teléfono:", persona[1])
    print("----------------")
