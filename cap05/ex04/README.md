# Exercício 5.4 - Funções

## Enunciado

Crie uma função que tenha dois parâmetros: `nome` e `idade`. A função deve imprimir na tela uma mensagem a seu gosto contendo o nome e a idade da pessoa. Em seguida, crie uma chamada para essa função passando argumentos de forma nomeada.

## Solução

```python
def imprime_nome_idade(nome, idade):
    print(f"O nome da pessoa é {nome} e a idade é {idade} anos.")

imprime_nome_idade(nome="João", idade=25)
```

## Explicação

Neste código, a função `imprime_nome_idade()` é definida com dois parâmetros, `nome` e `idade`. A função imprime uma frase que inclui o nome e a idade passados. Chamamos a função `imprime_nome_idade()` passando "João" para o parâmetro `nome` e 25 para o parâmetro `idade`. Esses argumentos são passados de forma nomeada, o que significa que especificamos os nomes dos parâmetros ao passar os argumentos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
