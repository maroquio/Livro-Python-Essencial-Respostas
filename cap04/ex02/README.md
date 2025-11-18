# Exercício 4.2 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir um número e calcule a raiz quadrada desse número. Ao fim, mostre o número como um valor monetário do Brasil.

## Solução

```python
import math
import locale

# Configura para o formato de moeda brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

numero = float(input("Insira um número: "))
raiz = math.sqrt(numero)

# Formata para moeda brasileira
valor_monetario = locale.currency(raiz, grouping=True)

print("A raiz quadrada do número informado é:", valor_monetario)
```

## Explicação

Nesta solução, utilizamos a biblioteca `math` para calcular a raiz quadrada e a biblioteca `locale` para formatar o número como um valor monetário do Brasil. Primeiro, pedimos ao usuário para inserir um número utilizando a função `input()`. O número inserido é convertido para `float` antes de calcular a raiz quadrada. Em seguida, calculamos a raiz quadrada utilizando `math.sqrt()`. Para apresentar o resultado como um valor monetário, usamos `locale.currency()` com a opção `grouping=True` para incluir separadores de milhar. Finalmente, o resultado é impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
