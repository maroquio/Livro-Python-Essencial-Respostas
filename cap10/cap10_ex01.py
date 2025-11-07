# Capítulo 10 - Exercício 1
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import multiprocessing
from time import perf_counter

def soma_numeros(numeros, retorno):
    retorno.put(sum(numeros))

if __name__ == "__main__":
    inicio = perf_counter()
    numeros = list(range(1, 99999999))
    metade = len(numeros) // 2
    retorno1 = multiprocessing.Queue()
    retorno2 = multiprocessing.Queue()
    processo1 = multiprocessing.Process(target=soma_numeros, args=(numeros[:metade], retorno1))
    processo2 = multiprocessing.Process(target=soma_numeros, args=(numeros[metade:], retorno2))
    processo1.start()
    processo2.start()
    processo1.join()
    processo2.join()
    resultado_final = retorno1.get() + retorno2.get()
    fim = perf_counter()
    print(f"A soma total é {resultado_final}")
    print(f"Tempo de execução: {fim - inicio:.2f} segundos.")
