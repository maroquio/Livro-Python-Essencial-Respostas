# Exercício 1.18 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar o valor da medida de um ângulo em radianos. Em seguida, o programa deve calcular e mostrar o valor desse ângulo em graus.

## Solução

```python
import math

angulo_radianos = float(input("Digite o valor do ângulo em radianos: "))

angulo_graus = angulo_radianos * 180 / math.pi

print(f"O ângulo em graus é: {angulo_graus:.2f}°")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite o valor de um ângulo em radianos, que é armazenado na variável `angulo_radianos`. Em seguida, é calculado o valor desse ângulo em graus, utilizando a fórmula ângulo em graus = ângulo em radianos * 180 / pi, onde `math.pi` é a constante pi importada do módulo `math`. O resultado é impresso utilizando o `print()`. O resultado é formatado com 2 casas decimais e a unidade de medida do ângulo (graus - °) é especificada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
