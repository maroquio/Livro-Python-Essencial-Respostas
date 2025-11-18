# Exercício 8.6 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Circulo` com um método `__init__` que inicialize o raio do círculo. Crie um método chamado `area` que retorne a área do círculo. Crie uma instância da classe `Circulo` e chame o método `area`.

## Solução

```python
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2

# Criando uma instância da classe Circulo
meu_circulo = Circulo(5)

# Chamando o método area para calcular a área do círculo
resultado_area = meu_circulo.area()
print(f"A área do círculo é: {resultado_area}")
```

## Explicação

Nesta solução, criamos a classe `Circulo`, que possui um construtor `__init__` para inicializar o raio do círculo. Também definimos o método `area`, que calcula e retorna a área do círculo utilizando a fórmula `area = $$ * $raio^2$`. Importamos o módulo `math` para obter o valor de $$ e calculamos a área do círculo com um raio de 5 unidades. Em seguida, chamamos o método `area` para calcular e exibir a área do círculo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
