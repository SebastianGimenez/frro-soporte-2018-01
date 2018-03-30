import random

class Persona:
	"""docstring for Persona"""

	nombre 	= ""
	edad 	= ""
	sexo 	= "" # H => hombre, M => mujer
	peso 	= ""
	altura 	= ""
	dni 	= ""
	def __init__(self, datos):
		self.nombre = datos["nombre"]
		self.edad 	= datos["edad"]
		self.sexo 	= datos["sexo"]
		self.peso 	= datos["peso"]
		self.altura = datos["altura"]
		self.dni 	= self.generar_dni()


	def es_mayor_edad(self):
		return True if (int(self.edad) >= 18) else False

	def print_data(self):
		cadena = "\n Nombre:{0}\n Edad:{1}\n Sexo:{2}\n Peso:{3}\n Altura:{4}\n Dni:{5}\n".format(self.nombre, self.edad, self.sexo, self.peso, self.altura, self.dni)
		print(cadena)

	def generar_dni(self):
		dni = ""
		for x in range(1,9):
			num = random.randint(0, 9)
			dni = dni + str(num)
		return dni


dicc = { "nombre":"", "edad":"", "sexo":"", "peso":"", "altura":"" }
for key in dicc:
	dicc[key] = input("Ingrese "+key+": ")

persona = Persona(dicc)
persona.print_data()
print("¿Es mayor de edad? ", persona.es_mayor_edad())