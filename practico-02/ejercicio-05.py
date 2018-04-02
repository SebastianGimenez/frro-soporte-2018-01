import random
from datetime import datetime

class Persona:
	def __init__(self, datos):
		self.nombre = datos["nombre"]
		self.edad 	= int(datos["edad"])
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

class Estudiante(Persona):
	def __init__(self, datos):
		Persona.__init__(self, datos)
		self.carrera 		= datos["carrera"]
		self.año_ingreso 	= int(datos["año_ingreso"])
		self.cant_materia 	= int(datos["cant_materia"])
		self.aprobadas 		= int(datos["aprobadas"])
	def avance(self):
		return (self.aprobadas*100)/self.cant_materia
	def edad_ingreso(self):
		if(self.es_mayor_edad()):
			#datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			año_actual = int(datetime.now().strftime('%Y'))
			return self.edad - (año_actual - self.año_ingreso)
		else: 
			return "Todavía no esta en la universidad, pues no es mayor de edad"


lista_estudiantes = []
def armar_lista():
	cadena = "\n 1. Ingresar Estudiante\n 0. Salir\n"
	print(cadena)
	opc = int(input("Ingrese una opción: \t"))

	while opc != 0:	
		dicc = { "nombre":"", "edad":"", "sexo":"", "peso":"", "altura":"", "carrera":"", "año_ingreso":"", "cant_materia":"", "aprobadas":"" }
		for key in dicc:
			plus = " [M / F]" if (key=="sexo") else ""
			dicc[key] = input("Ingrese "+key.replace("_", " ")+plus+": ")

		persona = Estudiante(dicc)
		lista_estudiantes.append(persona)

		print(cadena)
		opc = int(input("Ingrese una opción: \t"))

def armar_diccionario(lista):
	dicc = {}
	for obj in lista:
		if obj.carrera in dicc:
			dicc[obj.carrera] += 1
		else:
			dicc[obj.carrera] = 1
	return dicc


armar_lista()
dicc_carreras = armar_diccionario(lista_estudiantes)
for k, v in dicc_carreras.items():
	print(k, ": ", v)