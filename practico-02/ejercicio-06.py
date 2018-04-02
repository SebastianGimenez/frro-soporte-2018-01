from datetime import datetime

class Persona:
 	def __init__(self, nacimiento):
 		self.nacimiento =  datetime.strptime(nacimiento, '%d/%m/%Y')
 	
 	def edad(self):
 		return datetime.now().year - self.nacimiento.year

fecha_str = input("Ingrese fecha de nacimiento [ formato: dd/mm/YYYY ]:\t")
persona = Persona(fecha_str)
print("La edad de la persona es: ", persona.edad(), " años.")