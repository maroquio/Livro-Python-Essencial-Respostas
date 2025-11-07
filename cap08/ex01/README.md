# Exercício 8.1 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Pessoa` com um método `\_\_init\_\_` que inicialize o nome e a idade da pessoa. Crie um método chamado `mostrar\_dados` que exiba o nome e a idade da pessoa. Crie duas instâncias da classe `Pessoa` e chame o método `mostrar\_dados` de cada uma das instâncias.

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

Nesta solução, criamos a classe `Pessoa`, que possui um construtor `\_\_init\_\_` para inicializar o nome e a idade da pessoa. Também definimos o método `mostrar\_dados`, que imprime o nome e a idade da pessoa na tela. Em seguida, criamos duas instâncias da classe `Pessoa` com nomes e idades diferentes e chamamos o método `mostrar\_dados` para cada instância, exibindo os dados de cada pessoa no console.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
