from personal_academico.Docente import *
class Alumno:#Creamos la clase Alumno
	def __init__(self, nom ,doce_m, doce_s):
		self.nombres = nom
		self.docente_matematica = doce_m
		self.docente_sociales = doce_s

	#Metdos de agregar y obtener para los atributos de la clase
	def agregar_nombres(self, nomb):
		self.nombres = nomb
	
	def obtener_nombres(self):
		return self.nombres

	def agregar_docente_matematica(self, doce_mate):
		self.doce_matematica = doce_mate

	def obtener_docente_matematica(self):
		return self.docente_matematica.presentar_datos()

	def agregar_docente_sociales(self, doce_soci):
		self.doce_sociales = doce_soci

	def obtener_docente_sociales(self):
		return self.docente_sociales.presentar_datos()

	#Metodo para presentar datos
	def presentar_datos(self):
		cadena = "\nNombre de alumno: %s\n\nDocente matemáticas:\t%s\nDocente sociales:\t%s \n"%(self.obtener_nombres(),self.obtener_docente_matematica(),self.obtener_docente_sociales())
		return cadena