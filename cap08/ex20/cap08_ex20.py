# Capítulo 8 - Exercício 20
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        return f"{self.numerador}/{self.denominador}"

    def multiplicar(self, outra_fracao):
        numerador_resultante = self.numerador * outra_fracao.numerador
        denominador_resultante = self.denominador * outra_fracao.denominador
        return Fracao(numerador_resultante, denominador_resultante)

fracao1 = Fracao(1, 2)
fracao2 = Fracao(3, 4)
resultado = fracao1.multiplicar(fracao2)
print(fracao1.mostrar_dados())
print(resultado.mostrar_dados())
