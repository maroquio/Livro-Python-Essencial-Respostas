# Capítulo 5 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

vinhos = [
    {"nome": "Vinho A", "preco": 45},
    {"nome": "Vinho B", "preco": 80},
    {"nome": "Vinho C", "preco": 30},
    {"nome": "Vinho D", "preco": 60},
    {"nome": "Vinho E", "preco": 120}
]

vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))
print(vinhos_caros)
