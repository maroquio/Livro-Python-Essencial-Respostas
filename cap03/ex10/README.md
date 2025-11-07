# Exercício 3.10 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre todos os números primos de 1 a 100.

## Solução

```python
for num in range(1, 101):
    if num > 1:  # os números primos são maiores que 1
        for i in range(2, num):
            if (num % i) == 0:  # se o número é divisível por i, não é primo
                break
        else:  # se o laço não foi interrompido, o número é primo
            print(num)
```

## Explicação

Neste programa, o laço `for` externo itera sobre uma sequência de números de 1 a 100. O laço `for` interno itera sobre uma sequência de números de 2 a `num - 1`. Para cada número na sequência externa, verificamos se ele é divisível por algum número na sequência interna. Se for divisível, não é primo e interrompemos o laço interno. Se o laço interno terminar sem ser interrompido, o número é primo e é impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
