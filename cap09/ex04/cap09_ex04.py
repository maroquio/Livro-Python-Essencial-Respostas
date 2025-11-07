# Capítulo 9 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
