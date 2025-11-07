# Exercício 8.17 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Circulo` com um método `__init__` que inicialize o raio do círculo. Crie um método chamado `area` que calcule a área do círculo. Crie uma classe chamada `Cilindro` que herde da classe `Circulo`, adicione o atributo `altura` e um método chamado `volume` que calcule o volume do cilindro. Crie uma instância da classe `Cilindro` com uma determinada altura e chame o método `area` e o método `volume`, mostrando os resultados.

## Solução

```python
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def volume(self):
        return self.area() * self.altura

cilindro = Cilindro(3, 5)
print(cilindro.area())
print(cilindro.volume())
```

## Explicação

O código acima começa com a definição de uma classe `Circulo`, com um método de inicialização que aceita o raio do círculo como parâmetro. O método `area` da classe `Circulo` calcula e retorna a área do círculo usando a fórmula conhecida, que é `$$ * $raio^2$`. Em seguida, a classe `Cilindro` é definida, herdando da classe `Circulo`. Além do raio, o método de inicialização dessa classe também aceita a altura do cilindro. O método `volume` calcula e retorna o volume do cilindro, que é a área da base (um círculo, cuja área é obtida usando o método `area` herdado da classe `Circulo`) multiplicada pela altura. Finalmente, uma instância da classe `Cilindro` é criada com um raio de 3 e uma altura de 5, e os métodos `area` e `volume` são chamados nessa instância.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
