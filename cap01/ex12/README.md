# Exercício 1.12 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar as dimensões de um retângulo (largura e altura). Em seguida, o programa deve calcular e mostrar a área e o perímetro desse retângulo.

## Solução

```python
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Área do retângulo: {area:.2f}")
print(f"Perímetro do retângulo: {perimetro:.2f}")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite a largura e altura de um retângulo, que são armazenados nas variáveis `largura` e `altura`. Em seguida, são calculados a área e o perímetro do retângulo utilizando as fórmulas correspondentes da geometria e impressos utilizando o `print()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
