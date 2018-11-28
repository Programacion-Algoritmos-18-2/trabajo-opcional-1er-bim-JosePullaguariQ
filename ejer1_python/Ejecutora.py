#Importamos la clase Futnolista que esta en la carpeta modelo
from modelo.Futbolista import *

#Creamos el primer objeto tipo futbolista
f1 = Futbolista()
equipo1 = Equipo()#Creamos un el objeto 1 tipo Equipo

#Agregarmos los datos al equipo1 y al objeto tipo Futbolista
equipo1.agregar_nombre_equipo("Manchester United")
equipo1.agregar_pais("Inglaterra")
f1.agregar_nombre("Antonio")
f1.agregar_apellido("Valencia")
f1.agregar_equipo(equipo1)
f1.agregar_posicion("LATERAL")
f1.agregar_dorsal(25)
print(f1.presentar_datos())#Presentamos los datos

#Creamos el segundo objeto tipo futbolista
f2 = Futbolista()
equipo2 = Equipo()#Creamos un el objeto 2 tipo Equipo

#Agregarmos los datos al equipo1 y al objeto tipo Futbolista
equipo2.agregar_nombre_equipo("Necaxa")
equipo2.agregar_pais("México")
f2.agregar_nombre("Alex")
f2.agregar_apellido("Aguinaga")
f2.agregar_equipo(equipo2)
f2.agregar_posicion("MEDIOCENTRO")
f2.agregar_dorsal(7)
print(f2.presentar_datos())#Presentamos los datos

#Creamos el tercer objeto tipo futbolista
f3 = Futbolista()
equipo3 = Equipo()#Creamos un el objeto 3 tipo Equipo

#Agregarmos los datos al equipo 3 y al objeto tipo Futbolista
equipo3.agregar_nombre_equipo("Lazio")
equipo3.agregar_pais("Italia")
f3.agregar_nombre("Felipe")
f3.agregar_apellido("Caicedo")
f3.agregar_equipo(equipo1)
f3.agregar_posicion("DELANTERO")
f3.agregar_dorsal(32)
print(f3.presentar_datos())#Presentamos los datos