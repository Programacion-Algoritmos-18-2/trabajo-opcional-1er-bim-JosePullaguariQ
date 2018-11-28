class Garante(object):#Creamos la clase Garante 
	#Constructor de la clase
	def __init__(self, nom, ape, suel):					
		self.nombre = nom
		self.apellido = ape
		self.sueldo = suel

	#Metodos de agregar y obtener para los atributos de la clase
	def agregar_nombre(self,nom): 
		self.nombre = nom

	def agregar_apellido(self,ape):
		self.apellido = ape

	def agregar_sueldo(self,suel):
		self.sueldo = suel

	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_sueldo(self):
		return self.sueldo

	#Metodo para presentar datos
	def presentar_datos(self):
		cadena="Garante:\n\tNombre: %s %s\n\tSueldo: %d"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_sueldo())
		return cadena


class Prestamo(object):#Creamos la clase Prestamo
	#Constructor de la clase
	def __init__(self, nomB, suel, monP, inte, tiem, gar1):
		self.nombreBeneficiario = nomB 
		self.sueldo = suel
		self.montoPrestamo = monP
		self.interes = inte
		self.tiempo = tiem
		self.garante1= gar1

	#Metodos de agregar y obtener
	def agregar_nombre_beneficiario(self, nomB):
		self.nombreBeneficiario = nomB
		
	def agregar_sueldo(self, suel):
		self.sueldo = suel

	def agregar_monto_prestamo(self, monP):
		self.montoPrestamo = monP

	def agregar_interes(self,inte):
		self.interes = inte

	def agregar_tiempo(self,tiem):
		self.tiempo = tiem

	def agregar_garante1(self,gar1):
		self.garante1 = gar1

	def obtener_nombre_beneficiario(self):
		return self.nombreBeneficiario

	def obtener_sueldo(self):
		return	self.sueldo

	def obtener_monto_prestamos(self):
		return self.montoPrestamo

	def obtener_interes(self):
		return self.interes

	def obtener_tiempo(self):
		return self.tiempo

	def obtener_garante1(self):
		return self.garante1.presentar_datos()

	#Metodo para presentar datos
	def presentar_datos(self):										
		cadena="\nPrestamo:\n\tNombre del Beneficiario: %s\n\tSueldo: %d\n\tMonto Prestamos: %d\n\tInteres: %d\n\tTiempo: %d\n\t%s"%(self.obtener_nombre_beneficiario(),self.obtener_sueldo(),self.obtener_monto_prestamos(),self.obtener_interes(),self.obtener_tiempo(),self.obtener_garante1())
		return cadena


class PrestamoAutomovil(Prestamo):#Creamos la clase prestamos automovil que hereda de prestamo
	#Constructor de la clase
	def __init__(self, nomB, suel, momP, inte, tiem, gar1, tipov, marcav, gar2):						
		super(PrestamoAutomovil, self).__init__(nomB,suel,momP,inte,tiem,gar1)	
		self.tipo_vehiculo = tipov
		self.marca_vehiculo = marcav
		self.garante2 = gar2

	#Metodos de agregar y obtener para los atributos de la clase
	def agregar_tipo_vehiculo(self,tipov):
		self.tipo_vehiculo= tipov

	def agregar_marca_vehiculo(self,marcav):
		self.marca_vehiculo = marcav

	def agregar_garante2(self,gar2):
		self.garante2 = gar2

	def obtener_tipo_vehiculo(self):
		return self.tipo_vehiculo

	def obtener_marca_vehiculo(self):
		return self.marca_vehiculo

	def obtener_garante2(self):
		return self.garante2.presentar_datos()

	#Metodos para presentar datos
	def presentar_datos(self):
		cadena="\nPréstamo de Automóvil:\n\tNombre del Beneficiario: %s\n\tSueldo: %d\n\tMonto de Prestamos: %d\n\tInteres: %d\n\tTiempo: %d\n\tTipo de Vehiculo: %s\n\tMarca de Vehiculo: %s\n\t%s\n"%(self.obtener_nombre_beneficiario(),self.obtener_sueldo(),self.obtener_monto_prestamos(),self.obtener_interes(),self.obtener_tiempo(),self.obtener_tipo_vehiculo(),self.obtener_marca_vehiculo(),self.obtener_garante2())
		return cadena