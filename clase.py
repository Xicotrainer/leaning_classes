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
	def hablar(self): pass


class Deportista(Persona):

	# Sobreescritura del constructor 
	def __init__(self, edad, nombre, deporte):
		self.edad = edad
		self.nombre = nombre
		# Encapsulamiento del atributo deporte
		self.__deporte = deporte

		print("Se ha creado a {} con {} años de edad y practica {}.\n".
			format(self.nombre, self.edad, self.verDeporte()))

	def practicarDeporte(self):
		print("{}: Voy a practicar\n".
				format(self.nombre))

	def verDeporte(self):
		return self.__deporte

	# Tuplas 
	def hablar(self, *palabras):
		for frase in palabras:
			print ("{}: {} \n".
				format(self.nombre, frase))


# Instancias
Aragorn = Persona(37, "Aragorn")
Boromir = Persona(36, "Boromir")

Aragorn.hablar(["Voy a ser el prota en la parte III.","Me guta, hmmm jmm."])

Boromir.hablar(
	"A mi me carga chandingas en la peli I.", 
	"Oh rayios!!!")

# Instancia de la nueva clase
Michael = Deportista(35,  "Michael", "natación")
Michael.practicarDeporte()

Michael.hablar(
	"Me llaman la bala de Baltimor y no me gusta mi segundo nombre, Fred.",
	"Debute en el 2000 y con un total de 28 medallas en mi carrera profesional",
	"y me retiré en el 2016.")