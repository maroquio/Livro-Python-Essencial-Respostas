# Exercício 3.14 - Estruturas de Repetição

## Enunciado

Crie um programa que verifique se um número digitado pelo usuário é primo.

## Solução

```python
num = int(input("Digite um número: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} não é um número primo")
            break
    else:
        print(f"{num} é um número primo")
else:
    print(f"{num} não é um número primo")
```

## Explicação

Esse programa verifica se um número é primo. Primeiro, lê um número inteiro do usuário. Se o número for maior que 1, ele verifica se o número é divisível por algum número na sequência de 2 a `num - 1`. Se o número for divisível, ele não é primo, então o programa imprime uma mensagem indicando isso e interrompe o laço. Se o laço terminar sem ser interrompido, o número é primo, então o programa imprime uma mensagem indicando isso. Se o número for menor ou igual a 1, o programa imprime uma mensagem indicando que o número não é primo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
