# Exercício 8.5 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Animal` com um método `__init__` que inicialize o nome e a idade do animal. Crie um método chamado `emitir_som` que exiba um som genérico do animal. Crie uma instância da classe `Animal` e chame o método `emitir_som`.

## Solução

```python
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Som genérico do animal.")

# Criando uma instância da classe Animal
meu_animal = Animal("Cachorro", 3)

# Chamando o método emitir_som para o animal
meu_animal.emitir_som()
```

## Explicação

Nesta solução, criamos a classe `Animal`, que possui um construtor `__init__` para inicializar o nome e a idade do animal. Também definimos o método `emitir_som`, que exibe um som genérico do animal. Em seguida, criamos uma instância da classe `Animal` com um nome "Cachorro" e idade 3 e chamamos o método `emitir_som` para o animal, que imprimirá "Som genérico do animal" no console.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
