# Exercício 3.12 - Estruturas de Repetição

## Enunciado

(Difícil) Crie um programa que calcule e mostre a soma de todos os números primos de 1 a 100.

## Solução

```python
soma = 0
for num in range(1, 101):
    if num > 1:  # os números primos são maiores que 1
        for i in range(2, num):
            if (num % i) == 0:  # se o número é divisível por i, não é primo
                break
        else:  # se o laço não foi interrompido, o número é primo
            soma += num
print(soma)
```

## Explicação

Este código é similar ao do exercício 3.10, mas em vez de imprimir cada número primo, nós adicionamos os números primos à variável `soma` (isso é feito com a operação `soma += num`). Ao fim do laço externo, imprimimos a `soma`, que é a soma de todos os números primos de 1 a 100.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
