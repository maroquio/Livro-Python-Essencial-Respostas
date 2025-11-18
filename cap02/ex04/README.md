# Exercício 2.4 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um ano é bissexto ou não (pesquise o que caracteriza um ano como bissexto).

## Solução

```python
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um ano e armazenamos o valor na variável `ano`. Em seguida, verificamos se o ano é bissexto usando a estrutura condicional `if` e a regra para anos bissextos: um ano é bissexto se for divisível por 4 e não divisível por 100, ou se for divisível por 400. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
