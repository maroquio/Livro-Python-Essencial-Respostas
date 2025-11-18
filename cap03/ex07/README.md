# Exercício 3.7 - Estruturas de Repetição

## Enunciado

Crie um programa que leia vários números positivos digitados pelo usuário, até que ele digite um valor negativo. Ao fim, o programa deve mostrar a média dos números positivos digitados.

## Solução

```python
soma = 0
cont = 0
num = int(input("Digite um número positivo (ou um negativo para sair): "))
while num >= 0:
    soma += num
    cont += 1
    num = int(input("Digite um número positivo (ou um negativo para sair): "))
media = soma / cont
print(f"A média dos números positivos digitados é {media}")
```

## Explicação

Neste código, usamos um laço `while` que continua pedindo números ao usuário até que ele digite um valor negativo. A cada iteração, adicionamos o número digitado à `soma` e incrementamos o contador `cont`. Quando o usuário digita um número negativo, saímos do laço e calculamos a média dos números positivos dividindo a `soma` pelo `cont`. Por fim, imprimimos a média.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
