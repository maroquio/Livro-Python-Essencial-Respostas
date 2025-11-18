# Exercício 1.7 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar um número inteiro. Em seguida, o programa deve calcular e mostrar o valor dos inteiros anterior e posterior a esse número.

## Solução

```python
num = int(input("Digite um número: "))

print(f"Anterior: {num-1}")
print(f"Posterior: {num+1}")
```

## Explicação

O código utiliza a função *input()* para solicitar que o usuário digite um número, que é armazenado na variável *num*. Em seguida, é calculado o número anterior e posterior utilizando operações matemáticas, imprimindo-os ao fim utilizando a função *print()*.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
