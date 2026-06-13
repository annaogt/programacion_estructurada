# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")

def funcion1():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellido: ").strip().upper()
    print(f"El nombre de el alumno es: {nombre} {apellidos}")

def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre de el alumno es: {nombre} {apellidos}")

def funcion2():
    numero=int(8+5)
    return numero
   
def funcion4(nom, ape):
    nombre=nom
    apellidos=ape
   
    return nombre, apellidos


borrarPantalla()

