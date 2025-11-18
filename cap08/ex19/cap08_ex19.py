# Capítulo 8 - Exercício 19
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
