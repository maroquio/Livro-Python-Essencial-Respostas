# Exercício 4.4 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir um número e calcule o logaritmo natural desse número.

## Solução

```python
import math

# Solicita ao usuário um número
num = float(input("Digite um número: "))

# Calcula o logaritmo natural do número
log = math.log(num)

# Imprime o resultado
print(f"O logaritmo natural de {num} é {log}")
```

## Explicação

Nesta solução, o programa solicita ao usuário que insira um número. O programa então calcula o logaritmo natural desse número usando a função `math.log()`, que calcula o logaritmo natural de um número no Python. Note que, caso o número seja 0 ou negativo, a função `math.log()` resultará em um erro, pois o logaritmo natural não é definido para esses números. Finalmente, o resultado é impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
