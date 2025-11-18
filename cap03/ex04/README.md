# Exercício 3.4 - Estruturas de Repetição

## Enunciado

Crie um programa que some e mostre todos os números de 1 a 100.

## Solução

```python
soma = 0
for i in range(1, 101):
    soma += i
print(soma)
```

## Explicação

Neste código, inicializamos uma variável chamada `soma` com o valor 0 antes do laço `for`. Para cada número na sequência de 1 a 100, adicionamos esse número à `soma` (isso é feito com a operação `soma += i`). No final do laço, depois de somar todos os números, imprimimos o valor da `soma`, que é a soma de todos os números de 1 a 100.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
