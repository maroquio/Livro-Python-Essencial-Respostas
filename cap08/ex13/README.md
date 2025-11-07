# Exercício 8.13 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `ContaBancaria` com métodos para depositar, sacar e consultar o saldo da conta. Crie uma classe chamada `ContaPoupanca` que herde da classe `ContaBancaria` e adicione um atributo chamado `taxa_juros`, que corresponde à taxa de juros mensal. Em seguida, crie um método chamado `rendimento` na classe `ContaPoupanca` que calcule o rendimento mensal da conta, dado um número de meses como parâmetro. Crie uma instância da classe `ContaPoupanca` com uma taxa de juros de 0,5\%, faça um depósito de R\$ 1.000,00 e calcule o rendimento de 12 meses.

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
```

## Explicação

Na solução, criamos duas classes, `ContaBancaria` e `ContaPoupanca`. A classe `ContaBancaria` é uma representação simplificada de uma conta bancária com métodos para depositar e sacar fundos (`depositar` e `sacar`, respectivamente), bem como para verificar o saldo atual da conta (`consultar_saldo`). A classe `ContaPoupanca` é uma subclasse de `ContaBancaria`, herdando seus métodos e adicionando `taxa_juros` como atributo adicional. A `ContaPoupanca` possui um método adicional chamado `rendimento`, que calcula o rendimento da conta com base na taxa de juros, levando em consideração o número de meses como entrada. Isso é feito usando a fórmula de juros compostos. Finalmente, criamos uma instância da classe `ContaPoupanca`, depositamos um valor inicial e calculamos o rendimento após um período de 12 meses.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
