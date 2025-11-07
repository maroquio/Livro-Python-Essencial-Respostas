# Capítulo 8 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
