# Exercício 8.8 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `__init__` que inicialize o nome e a idade da pessoa, e um método chamado `mostrar_dados` que exiba o nome e a idade da pessoa. Crie uma classe chamada `Aluno` que herde da classe `Pessoa` e adicione um atributo `matricula` e um método `mostrar_dados` que exiba o nome, a idade e a matrícula do aluno. Crie uma instância da classe `Aluno` e chame o método `mostrar_dados`.

## Solução

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

# Criando uma instância da classe Aluno
aluno1 = Aluno("João", 20, "20230001")

# Chamando o método mostrar_dados para o aluno
aluno1.mostrar_dados()
```

## Explicação

Nesta solução, criamos a classe `Pessoa`, que possui um construtor `__init__` para inicializar o nome e a idade da pessoa, e o método `mostrar_dados`, que exibe o nome e a idade da pessoa. Em seguida, criamos a classe `Aluno`, que herda da classe `Pessoa` e adiciona um atributo `matricula` e o método `mostrar_dados`, que exibe o nome, a idade e a matrícula do aluno. Após a definição das classes, criamos uma instância da classe `Aluno`, chamada `aluno1`, com nome "João", idade 20 e matrícula "20230001". Em seguida, chamamos o método `mostrar_dados` para exibir os dados do aluno, incluindo seu nome, idade e matrícula.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
