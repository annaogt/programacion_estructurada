"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""



#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1

emails = []

cantidad = int(input("¿Cuántos correos deseas agregar?: "))

for i in range(cantidad):
    correo = input("Ingresa un correo: ")
    emails.append(correo)

print("Lista original:")
print(emails)

# Convertir la lista a set para eliminar duplicados
emails_unicos = set(emails)

print("Correos sin duplicados:")
print(emails_unicos)


#Solucion 2

correos = {
    "juan@utd.edu.mx",
    "ana@utd.edu.mx",
    "luis@utd.edu.mx",
    "juan@utd.edu.mx",
    "maria@utd.edu.mx"
}

print("Correos almacenados en el set:")
print(correos)



