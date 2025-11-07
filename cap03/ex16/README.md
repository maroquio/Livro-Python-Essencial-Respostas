# Exercício 3.16 - Estruturas de Repetição

## Enunciado

Crie um programa que encontre e mostre o maior e o menor número em uma lista de 10 números digitada pelo usuário.

## Solução

```python
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")
```

## Explicação

Esse programa lê 10 números do usuário e determina o maior e o menor número digitado. Primeiro, cria-se uma lista vazia chamada `numeros`. Em seguida, o programa usa um laço `for` para ler 10 números do usuário. Cada número digitado é adicionado à lista `numeros`. Depois, inicializamos as variáveis `maior` e `menor` com o primeiro número da lista. O programa então percorre cada número na lista: se um número é maior que o valor atual de `maior`, ele se torna o novo `maior`; se um número é menor que o valor atual de `menor`, ele se torna o novo `menor`. Ao fim do laço, `maior` e `menor` contêm o maior e o menor número da lista, respectivamente. Vale lembrar que esse problema pode ser resolvido de forma mais compacta usando as funções `min` e `max`, que serão vistas em um capítulo posterior.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
