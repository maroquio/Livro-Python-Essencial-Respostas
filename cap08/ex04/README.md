# Exercício 8.4 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Carro` com o atributo `velocidade` e com métodos para acelerar e frear o carro por X segundos, sendo que o carro acelera a 10m/s2 e freia a 5m/s2. Crie uma instância da classe `Carro` e teste os métodos criados.

## Solução

```python
class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        aceleracao = 10  # m/s²
        self.velocidade += aceleracao * segundos

    def frear(self, segundos):
        desaceleracao = 5  # m/s²
        self.velocidade -= desaceleracao * segundos

# Criando uma instância da classe Carro
meu_carro = Carro()

# Testando os métodos da classe
meu_carro.acelerar(5)
print(f"Velocidade atual: {meu_carro.velocidade}")
meu_carro.frear(2)
print(f"Velocidade atual após frear: {meu_carro.velocidade}")
```

## Explicação

Nesta solução, criamos a classe `Carro`, que possui o atributo `velocidade` e os métodos `acelerar` e `frear`. No construtor `__init__`, definimos o atributo `velocidade` com o valor inicial zero. O método `acelerar` recebe o número de segundos como argumento e aumenta a velocidade do carro usando uma aceleração constante de 10 m/s². O método `frear` recebe o número de segundos como argumento e diminui a velocidade do carro usando uma desaceleração constante de 5 m/s². Criamos uma instância da classe `Carro`, chamada `meu_carro`, e testamos os métodos `acelerar` e `frear`, exibindo a velocidade atual do carro após cada operação.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
