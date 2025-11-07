# Capítulo 3 - Exercício 18
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
