# Exercício 3.8 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre o fatorial de um número digitado pelo usuário.

## Solução

```python
num = int(input("Digite um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é {fatorial}")
```

## Explicação

O programa começa lendo um número inteiro do usuário. Em seguida, calcula o fatorial desse número usando um laço `for` que itera de 1 até o número digitado. O fatorial de um número é o produto de todos os inteiros positivos de 1 até esse número. Para calcular o fatorial, inicializamos a variável `fatorial` com 1 e, para cada número `i` no intervalo de 1 até o número digitado, multiplicamos `fatorial` por `i` (isso é feito com a operação `fatorial *= i`). Ao fim do laço, a variável `fatorial` contém o fatorial do número digitado, que então é impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
