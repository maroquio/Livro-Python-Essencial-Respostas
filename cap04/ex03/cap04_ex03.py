# Capítulo 4 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
