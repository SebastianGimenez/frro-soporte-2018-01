class Circulo:
	"""docstring for Circulo"""

	pi = 3.14156 #variables de clases

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * Circulo.pi
	
	def perimetro(self):
		return 2 * self.pi * self.radio


radio = int(input("Ingrese el radio del circulo: "))

circulo = Circulo(radio)
print("El area del círculo es: ", (circulo.area()))
print("El perimetro del círculo es: ", (circulo.perimetro()))