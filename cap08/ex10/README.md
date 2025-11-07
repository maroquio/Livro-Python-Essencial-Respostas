# Exercício 8.10 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `\_\_init\_\_` que inicialize o nome e a idade da pessoa. Crie um método chamado `mostrar\_dados` que exiba o nome e a idade da pessoa. Crie uma classe chamada `Cliente` que herde da classe `Pessoa` e adicione um atributo chamado `endereco`. Crie um método chamado `mostrar\_dados` na classe `Cliente` que exiba o nome, a idade e o endereço do cliente. Crie uma instância da classe `Cliente` e chame o método `mostrar\_dados`.

## Solução

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}")

# Criação de uma instância da classe Cliente
cliente = Cliente("João", 25, "Rua das Flores, 123")
cliente.mostrar_dados()
```

## Explicação

A classe `Pessoa` tem dois atributos, `nome` e `idade`, e um método `mostrar\_dados` que imprime o nome e a idade. A classe `Cliente` herda de `Pessoa`, adiciona um novo atributo, `endereco`, e sobrescreve o método `mostrar\_dados` para incluir o endereço na saída. A função `super()` é usada para chamar o método `\_\_init\_\_` da superclasse `Pessoa` e inicializar os atributos `nome` e `idade`. A instância da classe `Cliente` é criada com o nome "João", a idade de 25 anos e o endereço "Rua das Flores, 123", e o método `mostrar\_dados` é chamado para exibir essas informações.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
