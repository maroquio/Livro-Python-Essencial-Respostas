# Exercício 2.10 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se uma temperatura corporal digitada pelo usuário está acima, abaixo ou dentro da faixa normal (36°C a 37°C).

## Solução

```python
temperatura = float(input("Digite a temperatura corporal: "))

if temperatura < 36:
    print("A temperatura está abaixo da faixa normal.")
elif temperatura > 37:
    print("A temperatura está acima da faixa normal.")
else:
    print("A temperatura está dentro da faixa normal.")
```

## Explicação

Neste código, solicitamos ao usuário que digite a temperatura corporal e a convertemos para `float` antes de armazená-la na variável `temperatura`. Usamos a estrutura condicional `if` para verificar se a temperatura está abaixo, acima ou dentro da faixa normal (36°C a 37°C). Se a temperatura for menor que 36, imprimimos que está "abaixo da faixa normal". Se a temperatura for maior que 37, imprimimos que está "acima da faixa normal". Caso contrário, a temperatura está "dentro da faixa normal" e imprimimos a mensagem correspondente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
