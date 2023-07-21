
class Carro:
	
	def __init__(self, marca: str, modelo: str, ano: int):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano

	def apresentar_carro(self):
		print(f"{self.marca} - {self.modelo}({self.ano})")


def main():
	car = Carro('GM','Corsa',98)
	car.apresentar_carro()


if __name__=="__main__":
	main()
