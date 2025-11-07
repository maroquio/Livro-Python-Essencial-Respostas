# Exercício 8.7 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `__init__` que inicialize o nome e a idade da pessoa, e um método `mostrar_dados` que exiba o nome e a idade da pessoa. Crie uma classe chamada `Funcionario` que herde da classe `Pessoa` e adicione um atributo `salario` e um método chamado `mostrar_dados` que exiba o nome, a idade e o salário do funcionário. Crie uma lista com duas pessoas e dois funcionários e faça um laço para chamar o método `mostrar_dados` de todos os objetos dessa lista.

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

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}")

# Criando uma lista com pessoas e funcionários
pessoas_e_funcionarios = [
    Pessoa("João", 30),
    Pessoa("Maria", 25),
    Funcionario("Carlos", 40, 3000),
    Funcionario("Ana", 35, 2500)
]

# Chamando o método mostrar_dados para cada objeto da lista
for pessoa_ou_funcionario in pessoas_e_funcionarios:
    pessoa_ou_funcionario.mostrar_dados()
```

## Explicação

Nesta solução, criamos a classe `Pessoa`, que possui um construtor `__init__` para inicializar o nome e a idade da pessoa, e o método `mostrar_dados`, que exibe o nome e a idade da pessoa. Em seguida, criamos a classe `Funcionario`, que herda da classe `Pessoa` e adiciona um atributo `salario` e o método `mostrar_dados`, que exibe o nome, a idade e o salário do funcionário. 

Após a definição das classes, criamos uma lista chamada `pessoas_e_funcionarios` contendo objetos de ambas as classes (duas instâncias de `Pessoa` e duas instâncias de `Funcionario`). Em seguida, utilizamos um laço `for` para chamar o método `mostrar_dados` para cada objeto da lista, exibindo os dados de todas as pessoas e funcionários.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
