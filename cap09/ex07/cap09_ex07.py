# Capítulo 9 - Exercício 7
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise ValueError("Todos os lados devem ser maiores que zero.")
            if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
                raise ValueError("A soma de quaisquer dois lados deve ser maior que o terceiro lado.")
            if self.lado1 == self.lado2 == self.lado3:
                return "Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Isósceles"
            else:
                return "Escaleno"
        except ValueError as e:
            print(e)

triangulo = Triangulo(3, 4, 5)
print(triangulo.tipo_triangulo())
