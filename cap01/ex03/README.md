# Exercício 1.3 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distintas. Em seguida, imprima a média aritmética dos três números.

## Solução

```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

print(f"Média: {media}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite três números, que são armazenados nas variáveis `num1`, `num2` e `num3`. Em seguida, é calculada a média aritmética desses três números e armazenada na variável `media`. Por fim, o `print()` é utilizado para imprimir a variável `media`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
