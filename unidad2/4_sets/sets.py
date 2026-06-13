# """

 
#  Sets.- 
#   Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

#   Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
# """

print("\033c")

set1={"python", "SQL", "Estructurado"}
print(set1)

set2={"Hola", True, 33, 3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola " )
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)

lista=[10,9,5,8,2,3.4,8.5,10]
conjunto=set(lista)
lista=list(conjunto)
print(lista)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados


  
#Solucion 1
lista_emails=[]
set_emails={""}
opc="SI"
while opc=="SI":
    lista_emails.append(input("Ingresa un email: ").lower().strip())
    
    opc= input("Deseas agregar otro email (SI/NO): ").lower().strip()


set_emails=set(lista_emails)
lista_emails=list(set_emails)

print(lista_emails)
  

#Solucion 2
lista_emails=[]
set_emails={""}
opc=True
while opc==True:
    lista_emails.insert(0,input("Ingresa un email: ").lower().strip())
    
    opc= input("Deseas agregar otro email (S/N): ").lower().strip()
    if opc!="S":
        opc=False


set_emails=set(lista_emails)
lista_emails=list(set_emails)
print(lista_emails)


