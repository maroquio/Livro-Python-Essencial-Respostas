# Capítulo 10 - Exercício 2
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import multiprocessing

def soma_numeros(numeros, retorno):
    retorno.put(sum(numeros))

if __name__ == "__main__":
    numeros = list(range(1, 99999999))
    quarto = len(numeros) // 4
    retorno1 = multiprocessing.Queue()
    retorno2 = multiprocessing.Queue()
    retorno3 = multiprocessing.Queue()
    retorno4 = multiprocessing.Queue()
    processo1 = multiprocessing.Process(target=soma_numeros, args=(numeros[:quarto], retorno1))
    processo2 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto:quarto*2], retorno2))
    processo3 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto*2:quarto*3], retorno3))
    processo4 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto*3:], retorno4))
    processo1.start()
    processo2.start()
    processo3.start()
    processo4.start()
    processo1.join()
    processo2.join()
    processo3.join()
    processo4.join()
    resultado_final = retorno1.get() + retorno2.get() + retorno3.get() + retorno4.get()
    print(f"A soma total é {resultado_final}")
