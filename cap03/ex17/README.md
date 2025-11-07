# Exercício 3.17 - Estruturas de Repetição

## Enunciado

Crie um programa que encontre e mostre o segundo maior e o segundo menor números em uma lista de 10 números digitada pelo usuário.

## Solução

```python
numeros = []
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
maior = segundo_maior = float('-inf')
menor = segundo_menor = float('inf')
for num in numeros:
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num < maior and num > segundo_maior:
        segundo_maior = num
    if num < menor:
        segundo_menor = menor
        menor = num
    elif num > menor and num < segundo_menor:
        segundo_menor = num
print(f"O segundo maior número é {segundo_maior}")
print(f"O segundo menor número é {segundo_menor}")
```

## Explicação

O programa começa criando uma lista vazia chamada `numeros`. Em seguida, ele pede ao usuário para inserir 10 números e os adiciona à lista. Para encontrar o segundo maior e o segundo menor número, o programa primeiro define as variáveis `maior`, `segundo_maior`, `menor` e `segundo_menor` para valores inicialmente extremos (negativo infinito para `maior` e `segundo_maior` e positivo infinito para `menor` e `segundo_menor`). 

O programa, então, passa por cada número na lista. Se o número atual for maior que o valor atual de `maior`, o programa atualiza `segundo_maior` para o valor atual de `maior` e `maior` para o número atual. Se o número atual for menor que `maior` e maior que `segundo_maior`, o programa atualiza `segundo_maior` para o número atual. Um processo semelhante é seguido para encontrar o segundo menor número, atualizando `menor` e `segundo_menor` com base no número atual. Finalmente, o programa imprime o segundo maior e o segundo menor número. Vale ressaltar que esse problema poderia ser resolvido de forma mais compacta utilizando a função `sort()`, que é mostrada em um capítulo mais adiante.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
