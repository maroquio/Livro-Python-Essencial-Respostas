# Exercício 8.19 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Livro` com um método `__init__` que inicialize o título e o autor do livro. Crie um método chamado `mostrar_dados` que exiba o título e o autor do livro. Crie uma classe chamada `LivroDeBiblioteca` que herde da classe `Livro` e adicione um atributo chamado `codigo`. Crie um método chamado `mostrar_dados` na classe `LivroDeBiblioteca` que exiba o título, o autor e o código do livro. Crie uma instância da classe `LivroDeBiblioteca` e chame o método `mostrar_dados`.

## Solução

```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

class LivroDeBiblioteca(Livro):
    def __init__(self, titulo, autor, codigo):
        super().__init__(titulo, autor)
        self.codigo = codigo

    def mostrar_dados(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}"

livro = LivroDeBiblioteca("O Senhor dos Anéis", "J. R. R. Tolkien", "1234")
print(livro.mostrar_dados())
```

## Explicação

Nesse código, a classe base `Livro` possui um método `__init__` que inicializa o título e o autor do livro e um método `mostrar_dados` que retorna uma string com o título e o autor do livro. A classe `LivroDeBiblioteca` herda da classe `Livro` e adiciona um atributo `codigo` ao método `__init__`. Além disso, a classe `LivroDeBiblioteca` redefine o método `mostrar_dados` para incluir o código do livro na string retornada. Por fim, uma instância da classe `LivroDeBiblioteca` é criada com um título, autor e código, e o método `mostrar_dados` é chamado nessa instância.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
