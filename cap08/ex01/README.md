# Exercício 8.1 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `__init__` que inicialize o nome e a idade da pessoa. Crie um método chamado `mostrar_dados` que exiba o nome e a idade da pessoa. Crie duas instâncias da classe `Pessoa` e chame o método `mostrar_dados` de cada uma das instâncias.

## Solução

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Chamando o método mostrar_dados para cada instância
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
```

## Explicação

Nesta solução, criamos a classe `Pessoa`, que possui um construtor `__init__` para inicializar o nome e a idade da pessoa. Também definimos o método `mostrar_dados`, que imprime o nome e a idade da pessoa na tela. Em seguida, criamos duas instâncias da classe `Pessoa` com nomes e idades diferentes e chamamos o método `mostrar_dados` para cada instância, exibindo os dados de cada pessoa no console.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
