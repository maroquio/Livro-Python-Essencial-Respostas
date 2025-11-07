# Exercício 9.4 - Tratamento de Exceções

## Enunciado

Crie uma classe chamada `ContaBancaria` com os métodos `depositar` e `sacar`. Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada.

## Solução

```python
class SaldoInsuficienteError(Exception):
    def __init__(self):
        super().__init__("Saldo insuficiente para realizar o saque.")

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError()
        self.saldo -= valor

conta = ContaBancaria(100)
try:
    conta.sacar(50)
    print(conta.saldo)  # Deve imprimir 50
    conta.sacar(100)
except SaldoInsuficienteError as e:
    print(e)
```

## Explicação

Aqui, criamos uma exceção personalizada chamada `SaldoInsuficienteError` que herda da classe base `Exception` do Python, adicionando uma mensagem personalizada à exceção. A classe `ContaBancaria` possui um construtor que inicializa o atributo `saldo`, um método `depositar` que adiciona um valor ao saldo e um método `sacar` que subtrai um valor do saldo. Se o valor a ser sacado for maior do que o saldo disponível, lançamos a exceção personalizada `SaldoInsuficienteError`. As exceções lançadas pelo método `sacar` são capturadas no bloco `try`... `except` fora da classe, onde imprimimos a mensagem de erro.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
