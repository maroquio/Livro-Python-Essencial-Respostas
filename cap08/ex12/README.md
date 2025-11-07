# Exercício 8.12 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Veiculo` com métodos para acelerar, frear e exibir a velocidade do veículo. Crie uma classe chamada `Carro` que herde da classe `Veiculo` e adicione um atributo chamado `marca`. Crie uma instância da classe `Carro` e teste os métodos criados.

## Solução

```python
class Veiculo:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

    def mostrar_velocidade(self):
        print(f"Velocidade: {self.velocidade}")

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca

carro = Carro("Ford")
carro.acelerar(50)
carro.mostrar_velocidade()
carro.frear(20)
carro.mostrar_velocidade()
```

## Explicação

A classe `Veiculo` possui um atributo, `velocidade`, e três métodos: `acelerar`, que aumenta a velocidade; `frear`, que diminui a velocidade (mas não abaixo de zero); e `mostrar_velocidade`, que imprime a velocidade atual. A classe `Carro` herda de `Veiculo`, adicionando um atributo, `marca`. A instância da classe `Carro` é criada com a marca "Ford", depois o carro acelera por 50 unidades, a velocidade é exibida, o carro freia por 20 unidades, e a nova velocidade é exibida.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
