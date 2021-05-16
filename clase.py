class Persona:
	
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a {} con {} años de edad. \n".
			format(self.nombre, self.edad))

	# La sintaxis para diccionarios
	def hablar(self,**palabras):
		for frase in palabras:
			print ("{}: {} \n".
				format(self.nombre, palabras[frase]))


class Deportista(Persona):

	# Sobreescritura del constructor 
	def __init__(self, edad, nombre, deporte):
		self.edad = edad
		self.nombre = nombre
		self.deporte = deporte

		print("Se ha creado a {} con {} años de edad practicante de {}. \n".
			format(self.nombre, self.edad, self.deporte))

	def practicarDeporte(self):
		print("{}: voy a practicar\n".
				format(self.nombre))


# Instancias
Aragorn = Persona(37, "Aragorn")
Boromir = Persona(36, "Boromir")

Aragorn.hablar(
	f1 = "Voy a ser el prota en la parte III.", 
	f2 = "Me guta, hmmm jmm.")
Boromir.hablar(
	f1 = "A mi me carga chandingas en la peli I.", 
	f2 = "Oh rayios!!!")

# Instancia de la nueva clase
Michael_Phelps = Deportista(35,  "Michael", "Natación")
Michael_Phelps.practicarDeporte()

Michael_Phelps.hablar(
	f1 = "Me llaman la bala de Baltimor y no me gusta mi segundo nombre, Fred",
	f2 = "Debute en el 2000 y con un total de 28 medallas en mi carrera profesional",
	f3 = "me retiré en el 2016.")