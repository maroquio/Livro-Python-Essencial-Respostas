# Exercício 8.15 - Programação Orientada a Objetos

## Enunciado

Crie uma classe chamada `Produto` com um método `__init__` que inicialize o nome, o preço e a quantidade em estoque do produto. Crie também um método chamado `mostrar_dados` que exiba o nome, o preço e a quantidade em estoque do produto. Crie uma classe chamada `ProdutoImportado` que herde da classe `Produto` e adicione um atributo chamado `imposto`, que corresponde ao percentual de imposto que incide no respectivo produto. Crie um método chamado `preco_final` na classe `ProdutoImportado` que calcule o preço final do produto com o imposto adicionado. Crie uma instância da classe `ProdutoImportado` e chame o método `mostrar_dados` e o método `preco_final`.

## Solução

```python
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
```

## Explicação

A classe `Produto` possui os atributos `nome`, `preco` e `estoque`, além do método `mostrar_dados` para exibir essas informações. A classe `ProdutoImportado`, que herda de `Produto`, adiciona um atributo `imposto` e um método `preco_final` que calcula o preço final do produto, considerando o imposto. Uma instância da classe `ProdutoImportado` é criada com o nome "Camiseta", o preço R\$ 50,00, o estoque de 10 unidades e o imposto de 20\%. Em seguida, os métodos `mostrar_dados` e `preco_final` são chamados para exibir as informações do produto e o preço final, respectivamente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
