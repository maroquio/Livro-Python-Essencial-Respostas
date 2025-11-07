# Capítulo 8 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nPreço: R$ {self.preco}\nEstoque: {self.estoque} unidades")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, imposto):
        super().__init__(nome, preco, estoque)
        self.imposto = imposto
    def preco_final(self):
        return self.preco * (1 + self.imposto)

produto = ProdutoImportado("Camiseta", 50, 10, 0.2)
produto.mostrar_dados()
print(f"Preço final: R$ {produto.preco_final()}")
