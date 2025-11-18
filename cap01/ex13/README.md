# Exercício 1.13 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, o programa deve calcular e mostrar a área desse triângulo.

## Solução

```python
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = (base * altura) / 2

print(f"Área do triângulo: {area:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite a base e altura de um triângulo, que são armazenados nas variáveis `base` e `altura`. Em seguida, é calculada a área do triângulo utilizando a fórmula correspondente da geometria e impressa utilizando o `print()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
