class Persona:
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a {} con {} años de edad. \n".
			format(self.nombre, self.edad))

	# La sintaxis para tuplas
	def hablar(self, *palabras):
		for frase in palabras:
			print ("{}: {} \n".
				format(self.nombre, frase))

# Instancia
Aragorn = Persona(37, "Aragorn")
Boromir = Persona(36, "Boromir")
Aragorn.hablar("Voy a ser el prota en la parte III.", "Me guta, hmmm jmm.")
Boromir.hablar("A mi me carga chandingas en la I.", "Oh rayios!!!")