# Capítulo 8 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
