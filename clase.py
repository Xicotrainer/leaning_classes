class Persona:
	def __init__(self):
		self.edad = 18
		self.nombre = "Enebro"
		print("Se ha creado a", self.nombre, "con", self.edad, "años de edad.")

	def hablar(self, palabras = "Te voy a contar un chiste"):
		print (self.nombre,":", palabras)

# Instancia
Enebro = Persona()
Enebro.hablar()

Enebro.hablar("Esta por allí Vail, Aquiles")