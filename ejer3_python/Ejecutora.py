#Importamos la carpeta donde se encuentra el modelo 
from paquete.modelo import *					

#Creamos un objeto tipo Garante
garante1 = Garante("Juan","Morocho",500)					

#Creamos un objeto tipo Prestamo
p = Prestamo("Mario Alvarez",600, 20000, 10, 5, garante1)

#Creamos un objeto tipo Prestamo Automovil	
pa=PrestamoAutomovil("Sofia Velez",700,14000,8,9,garante1,"Convertible","Ferrari",Garante("Angie","Cardona",450))

#Presentamos los datos
print(p.presentar_datos())			
print(pa.presentar_datos())			