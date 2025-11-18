# Exercício 8.3 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `ContaBancaria` com o atributo `saldo` e com métodos para depositar, sacar e exibir o saldo da conta. Crie uma instância da classe `ContaBancaria` e teste os métodos criados.

## Solução

```python
class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual: {self.saldo}")

minha_conta = ContaBancaria()
minha_conta.depositar(1000)
minha_conta.exibir_saldo()
minha_conta.sacar(500)
minha_conta.exibir_saldo()
```

## Explicação

A solução para este exercício envolve a criação da classe `ContaBancaria`, que possui o atributo `saldo` e os métodos `depositar`, `sacar` e `exibir_saldo`. No construtor `__init__`, definimos o atributo `saldo` com o valor inicial zero. O método `depositar` aumenta o saldo da conta com o valor passado como argumento. O método `sacar` verifica se há saldo suficiente e, caso positivo, realiza o saque, diminuindo o saldo. Caso contrário, exibe uma mensagem informando que o saldo é insuficiente. O método `exibir_saldo` imprime o saldo atual da conta. Criamos uma instância da classe `ContaBancaria`, chamada `minha_conta`, e testamos os métodos `depositar`, `sacar` e `exibir_saldo`, exibindo o saldo após cada operação.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
