# Exercício 8.18 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Animal` com um método `\_\_init\_\_` que inicialize o nome do animal. Crie um método chamado `emitir\_som` que emita um som genérico do animal. Crie uma classe chamada `Cachorro` que herde da classe `Animal` e adicione um método chamado `emitir\_som` que emita o som do latido do cachorro. Crie uma instância da classe `Cachorro` e chame o método `emitir\_som`.

## Solução

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico do animal"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au Au"

cachorro = Cachorro("Totó")
print(cachorro.emitir_som())
```

## Explicação

O código acima define uma classe base `Animal` com um método `\_\_init\_\_` que inicializa o nome do animal e um método `emitir\_som` que retorna um som genérico do animal. Uma classe `Cachorro` é definida que herda da classe `Animal`. O método `emitir\_som` é substituído na classe `Cachorro` para retornar a onomatopeia do latido de um cachorro, que é "Au Au Au". Finalmente, uma instância da classe `Cachorro` é criada com o nome "Totó", e o método `emitir\_som` é chamado nessa instância.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
