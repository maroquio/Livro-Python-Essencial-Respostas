# Exercício 8.20 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Fracao` com um método `__init__` que inicialize o numerador e o denominador da fração. Crie um método chamado `mostrar_dados` que exiba a fração no formato "numerador/denominador". Crie um método chamado `multiplicar` que receba outra instância da classe `Fracao` como parâmetro e retorne uma nova instância da classe `Fracao` que represente a multiplicação das duas frações. Crie uma instância da classe `Fracao` e chame o método `mostrar_dados` e o método `multiplicar` com outra instância da classe `Fracao` como parâmetro.

## Solução

```python
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
```

## Explicação

Nesta solução, criamos a classe `Fracao` com um método de inicialização `__init__` que configura o numerador e o denominador da fração. Em seguida, adicionamos um método `mostrar_dados` que imprime a fração na tela no formato "numerador/denominador". Além disso, implementamos um método multiplicar que recebe outra instância da classe `Fracao` como parâmetro e retorna uma nova instância da classe `Fracao` que representa a multiplicação das duas frações. No bloco de testes, criamos duas instâncias da classe `Fracao`, `fracao1` e `fracao2`, e chamamos o método multiplicar na instância `fracao1`, passando `fracao2` como parâmetro. O resultado da multiplicação é armazenado em uma nova variável, `resultado`. Em seguida, o método `mostrar_dados` é chamado nas instâncias `fracao1` e `resultado` para imprimir as respectivas frações na tela.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
