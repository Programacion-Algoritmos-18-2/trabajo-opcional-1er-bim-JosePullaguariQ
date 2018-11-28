#Importamos la clase modelo
from personal_academico.Docente import *
from sector_estudiantil.Alumno import *

#Creamos el objeto 1 e tipo Docente
doce1 = Docente()
nombreDoce1 = input("Ingrese nombre del Docente matemáticas\n")
doce1.agregar_nombre(nombreDoce1)
apellidoDoce1 = input("Ingrese el apellido del Docente matemáticas\n")
doce1.agregar_apellido(apellidoDoce1)
tituloDoce1 = input("Ingrese el titulo del docente matemáticas\n")
doce1.agregar_titulo(tituloDoce1)

#Creamos el objeto 2 e tipo Docente
doce2 = Docente()
nombreDoce2 = input("\nIngrese nombre del Docente sociales\n")
doce2.agregar_nombre(nombreDoce2)
apellidoDoce2 = input("Ingrese el apellido del Docente sociales\n")
doce2.agregar_apellido(apellidoDoce2)
tituloDoce2 = input("Ingrese el titulo del docente sociales\n")
doce2.agregar_titulo(tituloDoce2)

#Creamos el objeto e tipo Alumno
nombreAlum = input("\nIngrese nombre del alumno\n")
a = Alumno(nombreAlum, doce1, doce2)
print(a.presentar_datos())
