# Exercício 3.18 - Estruturas de Repetição

## Enunciado

Crie um programa que calcule e mostre a sequência de Fibonacci até o *n*-ésimo termo, onde *n* é digitado pelo usuário.

## Solução

```python
n = int(input("Quantos termos você quer mostrar? "))
t1, t2 = 0, 1
print(f"{t1} -> {t2}", end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1, t2 = t2, t3
    cont += 1
print(" -> Fim")
```

## Explicação

Esse programa imprime a sequência de Fibonacci até o *n*-ésimo termo, onde `n` é fornecido pelo usuário. Primeiro, o programa lê o número de termos desejado. Em seguida, define os dois primeiros termos da sequência de Fibonacci, `t1` e `t2`, como 0 e 1, respectivamente. O programa então entra em um laço `while` que continua até que `cont` seja maior que `n`. Em cada iteração do laço, o programa calcula o próximo termo da sequência de Fibonacci como a soma de `t1` e `t2`, atualiza `t1` e `t2` para os dois últimos termos e incrementa `cont`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
