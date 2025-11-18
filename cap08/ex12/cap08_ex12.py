# Capítulo 8 - Exercício 12
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Veiculo:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

    def mostrar_velocidade(self):
        print(f"Velocidade: {self.velocidade}")

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca

carro = Carro("Ford")
carro.acelerar(50)
carro.mostrar_velocidade()
carro.frear(20)
carro.mostrar_velocidade()
