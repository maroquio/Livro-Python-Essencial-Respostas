# Capítulo 8 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Criando uma instância da classe Retangulo
meu_retangulo = Retangulo(5, 10)

# Chamando o método area para calcular a área do retângulo
resultado_area = meu_retangulo.area()
print(f"A área do retângulo é: {resultado_area}")
