# Función para abstracciones importada de la libreria abc
from abc import ABCMeta, abstractmethod

class Persona:
	__metaclass__ = ABCMeta
	
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a {} con {} años de edad.\n".
			format(self.nombre, self.edad))

	@abstractmethod
	# La sintaxis para diccionarios
	def hablar(self, *dialogo):
		pass


class Deportista(Persona):

	# Sobreescritura del constructor 
	def __init__(self, edad, nombre, deporte):
		self.edad = edad
		self.nombre = nombre
		# Encapsulamiento del atributo deporte
		self.__deporte = deporte

		print("Se ha creado a {} con {} años de edad, es practicante de {}.\n".
			format(self.nombre, self.edad, self.verDeporte()))

	def practicarDeporte(self):
		print("{}: Voy a practicar\n".
				format(self.nombre))

	def verDeporte(self):
		return self.__deporte

	# Parametro para tuplas 
	def hablar(self, *dialogo):
		for linea in dialogo:
			print("{}: {} \n".
				format(self.nombre, linea))


# Instancia de la nueva clase
Michael = Deportista(35,  "Michael", "natación")

Michael.hablar(
	"Me llaman la bala de Baltimor, no me gusta mi segundo nombre: Fred.",
	"Debute en el 2000 y con un total de 28 medallas en mi carrera profesional,"
	"me retiré en el 2016."
	)