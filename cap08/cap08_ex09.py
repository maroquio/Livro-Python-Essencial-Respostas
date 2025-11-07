# Capítulo 8 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Criação de uma instância da classe Quadrado
quadrado = Quadrado(5)
print(quadrado.area())
