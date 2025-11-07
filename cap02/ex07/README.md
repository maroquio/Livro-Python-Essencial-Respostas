# Exercício 2.7 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um texto digitado pelo usuário é um número inteiro ou não e mostre uma mensagem de acordo (use a função `texto.isdigit` para verificar).

## Solução

```python
texto = input("Digite um texto: ")

if texto.isdigit():
    print("O texto é um número inteiro.")
else:
    print("O texto não é um número inteiro.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um texto e armazenamos o valor na variável `texto`. Verificamos se o texto é um número inteiro usando o método `isdigit()`. Se o método retornar `True`, o texto é um número inteiro; caso contrário, não é. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
