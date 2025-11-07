# Exercício 8.11 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `\_\_init\_\_` que inicialize o nome e a idade da pessoa. Crie um método chamado `mostrar\_dados` que exiba o nome e a idade da pessoa. Crie uma classe chamada `Funcionario` que herde da classe `Pessoa` e adicione um atributo chamado `salario`. Crie um método chamado `aumentar\_salario` na classe `Funcionario` que receba um valor de aumento e adicione ao salário atual. Crie uma instância da classe `Funcionario`, chame o método `aumentar\_salario` com um valor de aumento de 10\% e chame o método `mostrar\_dados`.

## Solução

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario += self.salario * aumento / 100

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}")

# Criação de uma instância da classe Funcionario
funcionario = Funcionario("Maria", 30, 3000)
funcionario.aumentar_salario(10)
funcionario.mostrar_dados()
```

## Explicação

Similar à solução anterior, a classe `Funcionario` herda de `Pessoa`, adicionando um atributo `salario` e um método `aumentar\_salario`, que calcula o novo salário após um aumento percentual. O método `mostrar\_dados` é sobrescrito para incluir o salário na saída. A instância da classe `Funcionario` é criada com o nome "Maria", a idade de 30 anos e o salário de 3000. O método `aumentar\_salario` é chamado com um aumento de 10\%, e o método `mostrar\_dados` é usado para exibir as informações atualizadas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
