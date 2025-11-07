# Capítulo 8 - Exercício 13
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
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros

    def rendimento(self, meses):
        return self.saldo * ((1 + self.taxa_juros)**meses - 1)

# Testando a classe ContaPoupanca
conta_poupanca = ContaPoupanca(0.005)  # taxa de juros de 0.5%
conta_poupanca.depositar(1000)  # deposita R$ 1.000,00
print(f"Saldo após 12 meses: R$ {conta_poupanca.rendimento(12):.2f}")
