# Capítulo 10 - Exercício 3
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import multiprocessing
import os

def filho():
    print(f"Processo filho com PID: {os.getpid()}")

if __name__ == "__main__":
    print(f"Processo pai com PID: {os.getpid()}")

    processo_filho = multiprocessing.Process(target=filho)
    processo_filho.start()
    processo_filho.join()
