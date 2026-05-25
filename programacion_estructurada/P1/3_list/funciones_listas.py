"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


# Lista de ejemplo
numeros = [5, 8, 2, 8, 1]

# Funciones más comunes en las listas


# Imprimir el contenido de una lista
print(numeros)


# Recorrer la lista
# 1er forma
for i in numeros:
    print(i)

# 2da forma
for i in range(len(numeros)):
    print(numeros[i])


# Ordenar elementos de una lista
numeros.sort()
print(numeros)


# Dar la vuelta a una lista
numeros.reverse()
print(numeros)


# Agregar, insertar, añadir un elemento a una lista
# 1er forma
numeros.append(10)
print(numeros)

# 2da forma
numeros.insert(2, 20)
print(numeros)


# Eliminar, borrar, suprimir un elemento de una lista
# 1er forma
numeros.remove(8)
print(numeros)

# 2da forma
numeros.pop()
print(numeros)


# Buscar un elemento dentro de la lista
print(5 in numeros)


# Contar el número de veces que aparece un elemento dentro de una lista
print(numeros.count(8))


# Conocer la posición o índice en el que se encuentra un elemento
print(numeros.index(20))


# Unir el contenido de una lista dentro de otra lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)
print(lista1)


# Crear a partir de las listas números 1 y 2
# un resultado y mostrar el contenido ordenado descendentemente

numeros1 = [3, 7, 1]
numeros2 = [8, 2, 5]

resultado = numeros1 + numeros2

resultado.sort(reverse=True)

print(resultado)







