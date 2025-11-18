# Exercício 4.6 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir dois números complexos e calcule a soma e o produto desses números.

## Solução

```python
num1 = complex(input("Digite o primeiro número complexo: "))
num2 = complex(input("Digite o segundo número complexo: "))

soma = num1 + num2
produto = num1 * num2

print(f"A soma dos números complexos é {soma}")
print(f"O produto dos números complexos é {produto}")
```

## Explicação

Na solução deste exercício, o usuário é solicitado a inserir dois números complexos. A função `complex()` é utilizada para converter as strings inseridas em números complexos. Em seguida, os números complexos são somados e multiplicados. Os resultados são impressos na tela.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
