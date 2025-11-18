# Capítulo 10 - Exercício 4
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import multiprocessing

def fatorial(n, retorno):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    retorno.put(fatorial)

if __name__ == "__main__":
    num = 10
    metade = num // 2

    retorno1 = multiprocessing.Queue()
    retorno2 = multiprocessing.Queue()

    processo1 = multiprocessing.Process(target=fatorial, args=(metade, retorno1))
    processo2 = multiprocessing.Process(target=fatorial, args=(num - metade, retorno2))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

    resultado_final = retorno1.get() * retorno2.get()
    print(f"O fatorial de {num} é {resultado_final}")
