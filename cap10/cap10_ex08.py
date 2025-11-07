# Capítulo 10 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import threading
import time
import random

def mostrar_numero(numero):
    atraso = random.randint(1, 4)
    time.sleep(atraso)
    print(f"Thread {numero} esperou por {atraso} segundos.")

if __name__ == "__main__":
    for i in range(1, 11):
        threading.Thread(target=mostrar_numero, args=(i,)).start()
