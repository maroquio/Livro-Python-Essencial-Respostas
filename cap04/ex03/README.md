# Exercício 4.3 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir um ângulo em graus e calcule o seno, o cosseno e a tangente desse ângulo.

## Solução

```python
import math

# Solicita ao usuário um ângulo em graus
angulo = float(input("Digite um ângulo em graus: "))

# Converte o ângulo para radianos
radianos = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Imprime os resultados
print(f"O seno de {angulo} é {seno}")
print(f"O cosseno de {angulo} é {cosseno}")
print(f"A tangente de {angulo} é {tangente}")
```

## Explicação

Na solução acima, o programa solicita ao usuário que insira um ângulo em graus. A função `math.radians()` é usada para converter o ângulo de graus para radianos, já que as funções trigonométricas no módulo `math` do Python requerem a entrada em radianos. Após isso, são calculados o seno, o cosseno e a tangente do ângulo usando as funções `math.sin()`, `math.cos()` e `math.tan()`, respectivamente. Finalmente, os resultados são impressos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
