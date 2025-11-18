# Exercício 8.16 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Triangulo` com um método `__init__` que inicialize os lados do triângulo, e um método chamado `perimetro` que calcule o perímetro do triângulo. Crie uma classe chamada `TrianguloRetangulo` que herde da classe `Triangulo` e adicione um método chamado `area` que calcule a área do triângulo retângulo. O construtor da classe `TrianguloRetangulo` deve receber somente os catetos como parâmetro, devendo calcular a hipotenusa. Ao fim, crie uma instância da classe `TrianguloRetangulo` e chame o método `perimetro` e o método `area`.

## Solução

```python
import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        return self.a + self.b + self.c

class TrianguloRetangulo(Triangulo):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2))
    def area(self):
        return 0.5 * self.a * self.b

triangulo = TrianguloRetangulo(3, 4)
print(f"Perímetro: {triangulo.perimetro()}")
print(f"Área: {triangulo.area()}")
```

## Explicação

A classe `Triangulo` possui os atributos `a`, `b` e `c`, representando os lados do triângulo, e um método `perimetro` que calcula o perímetro do triângulo. A classe `TrianguloRetangulo`, que herda de `Triangulo`, redefine o método `__init__` para calcular o terceiro lado (hipotenusa) usando o teorema de Pitágoras e adiciona um método `area` para calcular a área do triângulo retângulo. Uma instância da classe `TrianguloRetangulo` é criada com os lados 3 e 4. Em seguida, os métodos `perimetro` e `area` são chamados para calcular e exibir o perímetro e a área do triângulo retângulo, respectivamente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
