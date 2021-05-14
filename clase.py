class Persona:
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a {} con {} años de edad. \n".
			format(self.nombre, self.edad))

	def hablar(self, palabras = "Te voy a contar un chiste"):
		print ("{}: {} \n".
			format(self.nombre, palabras))

# Instancia
Aragorn = Persona(37, "Aragorn")
Boromir = Persona(36, "Boromir")
Aragorn.hablar("Voy a ser el prota en la parte III")
Boromir.hablar("A mi me carga chandingas desde el inicio. Oh rayios!!!")