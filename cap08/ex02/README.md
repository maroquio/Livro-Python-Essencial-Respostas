# Exercício 8.2 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Retangulo` com um método `__init__` que inicialize a largura e a altura do retângulo. Crie um método chamado `area` que retorne a área do retângulo. Crie uma instância da classe `Retangulo` e chame o método `area`.

## Solução

```python
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
```

## Explicação

Nesta solução, criamos a classe `Retangulo`, que possui um construtor `__init__` para inicializar os atributos `largura` e `altura` do retângulo. Além disso, definimos o método `area`, que calcula e retorna a área do retângulo, utilizando a fórmula `área = largura * altura`. Em seguida, criamos uma instância da classe `Retangulo`, passando os valores de largura e altura. Posteriormente, chamamos o método `area` da instância para calcular a área do retângulo e a exibimos no console.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
