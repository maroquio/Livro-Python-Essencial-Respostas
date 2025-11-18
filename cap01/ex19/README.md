# Exercício 1.19 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.

## Solução

```python
import math

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))

hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite o comprimento dos dois lados de um triângulo retângulo, que são armazenados nas variáveis `lado1` e `lado2`, respectivamente. Em seguida, é calculado o comprimento da hipotenusa do triângulo, utilizando a fórmula hipotenusa = raiz quadrada de (lado1² + lado2²), onde `math.sqrt()` é a função que calcula a raiz quadrada importada do módulo `math`. O resultado é impresso utilizando o `print()`. O resultado é formatado com 2 casas decimais e a unidade de medida do comprimento (unidade de medida dos lados) é especificada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
