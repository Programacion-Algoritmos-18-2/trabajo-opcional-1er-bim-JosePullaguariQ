class Futbolista():
	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.equipo = Equipo()
		self.posicion = " "
		self.dorsal = 0

	#Metdos de agregar y obtener para los atributos de la clase
	def agregar_nombre(self, n):
		self.nombre=n

	def obtener_nombre (self):
		return self.nombre

	def agregar_apellido(self, a):
		self.apellido = a

	def obtener_apellido(self):
		return self.apellido

	def agregar_equipo(self, e):
		self.equipo = e

	def obtener_equipo(self):
		return self.equipo

	def agregar_posicion(self, pos):
		self.posicion = pos

	def obtener_posicion(self):
		return self.posicion

	def agregar_dorsal(self, d):
		self.dorsal = d

	def obtener_dorsal(self):
		return self.dorsal

	#Metodo para presentar los datos
	def presentar_datos(self):
		cadena = "Jugador:\n \t%s %s,\n\tPertenece al equipo %s del pais %s,\n \tsu posición es %s y \n\tsu dorsal es el número %d.\n"%(self.nombre,self.apellido,self.equipo.obtener_nombre_equipo(),self.equipo.obtener_pais(),self.posicion,self.obtener_dorsal())
		return cadena

class Equipo(object):#Creamos la clase equipo
	def __init__(self):#Constructor de la clase
		self.nombre_equipo = " "
		self.pais = " "

	#Metdos de agregar y obtener para los atributos de la clase
	def agregar_nombre_equipo(self, n):
		self.nombre_equipo =n

	def obtener_nombre_equipo(self):
		return self.nombre_equipo

	def agregar_pais(self, p):
		self.pais = p

	def obtener_pais(self):
		return self.pais

	#Metodo para presentar los datos
	def presentar_datos(self):
		cadena = "\nNombre equipo: %s \n Pais equipo : %s"%(self.nombreq,self.pais)
		return cadena