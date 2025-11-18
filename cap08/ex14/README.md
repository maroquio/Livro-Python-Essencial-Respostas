# Exercício 8.14 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Livro` com um método `__init__` que inicialize o título e o autor do livro. Crie um método chamado `mostrar_dados` que exiba o título e o autor do livro. Crie uma classe chamada `LivroFisico` que herde da classe `Livro` e adicione um atributo chamado `paginas`. Crie um método chamado `mostrar_dados` na classe `LivroFisico` que exiba o título, o autor e o número de páginas do livro. Crie uma instância da classe `LivroFisico` e chame o método `mostrar_dados`.

## Solução

```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def mostrar_dados(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}")

class LivroFisico(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas
    def mostrar_dados(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}")

livro = LivroFisico("12 regras para a vida", "Jordan Peterson", 328)
livro.mostrar_dados()
```

## Explicação

A classe `Livro` tem os atributos `titulo` e `autor` e o método `mostrar_dados` para exibir essas informações. A classe `LivroFisico` herda da classe `Livro` e adiciona um atributo `paginas`. O método `mostrar_dados` na classe `LivroFisico` é substituído para também exibir o número de páginas. Uma instância da classe `LivroFisico` é criada com o título "12 regras para a vida", o autor "Jordan Peterson" e 328 páginas. Em seguida, o método `mostrar_dados` é chamado para exibir as informações do livro.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
