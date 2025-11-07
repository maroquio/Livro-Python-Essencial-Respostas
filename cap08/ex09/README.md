# Exercício 8.9 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Retangulo` com um método `__init__` que inicialize a largura e a altura do retângulo. Crie um método chamado `area` que retorne a área do retângulo. Crie uma classe chamada `Quadrado` que herde da classe `Retangulo` e substitua o método `__init__` para que seja necessário apenas informar um lado, ao invés de largura e altura. Crie uma instância da classe `Quadrado` e chame o método `area`.

## Solução

```python
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
```

## Explicação

Aqui, a classe `Retangulo` é criada com um método `__init__` que inicializa a largura e a altura do retângulo, e um método `area` que retorna a área do retângulo, calculada como o produto de sua largura e altura. A classe `Quadrado` é uma subclasse de `Retangulo`. Seu método `__init__` é substituído para aceitar apenas um único argumento - o lado do quadrado. A função `super()` é usada para chamar o método `__init__` da superclasse `Retangulo`, passando o mesmo valor para largura e altura, já que todos os lados de um quadrado são iguais. A instância da classe `Quadrado` é criada com o lado de 5 unidades, e o método `area` é chamado para calcular e imprimir a área do quadrado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
