class Laberinto:
	"""docstring for Laberinto"""
	entrada 	= []
	salida 		= []
	posicion  	= []
	tamaño		= []
	laberinto 	= []
	camino 		= []
	intentos	= 1
	
	def __init__(self):
		pass
	
	def resolver(self, laberinto):
		self.laberinto = laberinto
		self.encontrar_limites(laberinto)
		# print(self.entrada)
		# print(self.salida)
		self.mover()

		return self.camino			

	def mover(self):
		# print("entrada", self.entrada)
		# print("posicion", self.posicion)
		# if self.posicion == self.entrada:
		# 	if self.arrancar():
		# 		self.mover()
		# 	else:
		# 		print("No se puede arrancar, sucedio un problema.")
		# elif self.posicion == self.salida:
		# 	self.camino.append(self.salida)
		# 	print("Se resolvio el Laberinto!!")
		# else:

		if(self.intentos == 1):
			self.derecha()
			if (self.laberinto[self.posicion[0]][self.posicion[1]] == True): #Si no hay bloque, guardo el camino
				self.izquierda()
				self.intentos = self.intentos+1
			elif (self.laberinto[self.posicion[0]][self.posicion[1]] == "b"):
				print("que lindo encontro la salida :-)")
				return True
			else: #Si hay bloque, vuelvo a la posicion
				self.camino.append(self.posicion)
				self.intentos = 1
			
			self.mover()
		elif(self.intentos == 2):
			self.izquierda()
			if (self.laberinto[self.posicion[0]][self.posicion[1]] == True): #Si no hay bloque, guardo el camino
				self.derecha()
				self.intentos = self.intentos+1
			elif (self.laberinto[self.posicion[0]][self.posicion[1]] == "b"):
				print("que lindo encontro la salida :-)")
				return True
			else: #Si hay bloque, vuelvo a la posicion
				self.camino.append(self.posicion)
				self.intentos = 1
			
			self.mover()
		elif(self.intentos == 3):
			self.abajo()
			if (self.laberinto[self.posicion[0]][self.posicion[1]] == True): #Si no hay bloque, guardo el camino
				self.arriba()
				self.intentos = self.intentos+1
			elif (self.laberinto[self.posicion[0]][self.posicion[1]] == "b"):
				print("que lindo encontro la salida :-)")
				return True
			else: #Si hay bloque, vuelvo a la posicion
				self.camino.append(self.posicion)
				self.intentos = 1
			
			self.mover()
		elif(self.intentos == 4):
			self.arriba()
			if (self.laberinto[self.posicion[0]][self.posicion[1]] == True): #Si no hay bloque, guardo el camino
				self.abajo()
				self.intentos = self.intentos+1
			elif (self.laberinto[self.posicion[0]][self.posicion[1]] == "b"):
				print("que lindo encontro la salida :-)")
				return True
			else: #Si hay bloque, vuelvo a la posicion
				self.camino.append(self.posicion)
				self.intentos = 1
			
			self.mover()
		else:
			print("no encuentro camino :(")

		return False


	def encontrar_limites(self, laberinto):
		for y, lista in enumerate(laberinto):
			for x, valor in enumerate(lista):
				if valor == "a":
					self.entrada = [x, y]
					self.camino.append([x, y])
					self.posicion = [x, y]
					# print(valor)
				if valor == "b":
					self.salida = [x, y]
					# print(valor)

	def arriba(self):
		if (self.posicion[1] > 0):
			self.posicion[1] = (self.posicion[1] - 1)
		else:
			self.posicion[1] = 0
			
		# y = (self.posicion[1] - 1) if (self.posicion[1] > 0) else 0

	def abajo(self):
		if (self.posicion[1] < (len(self.laberinto)-1)):
			self.posicion[1] = (self.posicion[1] + 1)
		else:
			self.posicion[1] = (len(self.laberinto)-1)
			
		# y = (self.posicion[1] + 1) if (self.posicion[1] < (len(self.laberinto)-1)) else (len(self.laberinto)-1)

	def izquierda(self):
		if (self.posicion[0] > 0):
			self.posicion[0] = (self.posicion[0] - 1)
		else:
			self.posicion[0] = 0
			
		# x = (self.posicion[0] - 1) if (self.posicion[0] > 0) else 0

	def derecha(self):
		if (self.posicion[0] < (len(self.laberinto[self.posicion[1]])-1)):
			self.posicion[0] = (self.posicion[0] + 1)
		else:
			self.posicion[0] = (len(self.laberinto[self.posicion[1]])-1)
			
		# x = (self.posicion[0] + 1) if (self.posicion[0] < (len(self.laberinto[self.posicion[1]])-1)) else (len(self.laberinto[self.posicion[0]])-1)


laberinto = [
	[True, False, True, True],
	["a", False, False, True],
	[False, True, False, True],
	[False, True, False, "b"]
];

lab = Laberinto()
solucion = lab.resolver(laberinto);
print(solucion)
# print(len(laberinto))

# asd = [True, False, True, True]
# asd[1] = "asd"
# print(asd)