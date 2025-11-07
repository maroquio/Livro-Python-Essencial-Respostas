# Capítulo 8 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        aceleracao = 10  # m/s²
        self.velocidade += aceleracao * segundos

    def frear(self, segundos):
        desaceleracao = 5  # m/s²
        self.velocidade -= desaceleracao * segundos

# Criando uma instância da classe Carro
meu_carro = Carro()

# Testando os métodos da classe
meu_carro.acelerar(5)
print(f"Velocidade atual: {meu_carro.velocidade}")
meu_carro.frear(2)
print(f"Velocidade atual após frear: {meu_carro.velocidade}")
