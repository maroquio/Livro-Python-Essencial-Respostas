# Exercício 1.22 - Fundamentos da Linguagem

## Enunciado

Crie um programa que calcule e mostre o perímetro de um círculo dado o seu raio como entrada.

## Solução

```python
import math

raio = float(input("Digite o raio do círculo (m): "))

perimetro = 2 * math.pi * raio

print(f"Perímetro do círculo: {perimetro:.2f} m")
```

## Explicação

Neste código, importamos a biblioteca `math` para utilizar a constante `math.pi`. Em seguida, solicitamos ao usuário o raio do círculo e calculamos o perímetro utilizando a fórmula `perimetro = 2 * math.pi * raio`. Por fim, imprimimos o resultado formatado com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
