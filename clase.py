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

	def practicarDeporte(self):
		print("{}: voy a practicar\n".
				format(self.nombre))


# Instancias
Aragorn = Persona(37, "Aragorn")
Boromir = Persona(36, "Boromir")

Aragorn.hablar( f1 = "Voy a ser el prota en la parte III.", 
				f2 = "Me guta, hmmm jmm.")
Boromir.hablar( f1 = "A mi me carga chandingas en la peli I.", 
				f2 = "Oh rayios!!!")

# Legolas es un elfo.. ¿es una persosna?
Legolas = Deportista(2931, "Legolas")
Legolas.practicarDeporte()

Legolas.hablar( f1 = "No como Gimli",
				f2 = "Él es peligroso en distancias cortas", 
				f3 = "jajajjaja")