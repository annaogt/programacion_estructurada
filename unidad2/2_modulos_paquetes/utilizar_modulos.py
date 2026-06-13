# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()

n="Daniel"
a="Carreon"

nombre, apellidos=modulos.funcion4(n,a)
print(f"El nombre completo es: {nombre} {apellidos}")



#2da formar de utilizar modulos
from modulos import borrarPantalla, funcion3, funcion4

borrarPantalla()
n="Eleazar"
a="Gonzalez"

funcion3(n,a)

nombre, apellidos=funcion4(n,a)
print(f"El nombre completo es: {nombre} {apellidos}")

