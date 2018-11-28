class Docente:#Creamos la clase Docente
	def __init__(self):
		self.nombre = " " 
		self.apellido = " "
		self.titulo = " "
	
	#Metdos de agregar y obtener para los atributos de la clase
	def agregar_nombre(self, n):
		self.nombre = n
	
	def obtener_nombre(self):
		return self.nombre

	def agregar_apellido(self, a):
		self.apellido = a
	
	def obtener_apellido(self):
		return self.apellido

	def agregar_titulo(self, tit):
		self.titulo = tit
	
	def obtener_titulo(self):
		return self.titulo

	#Metodo para presentar datos
	def presentar_datos(self):
		cadena = "\nNombre: %s Apellido: %s Titulo:%s\n"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_titulo())
		return cadena