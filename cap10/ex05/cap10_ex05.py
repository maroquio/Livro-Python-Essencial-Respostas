# Capítulo 10 - Exercício 5
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import multiprocessing
import time

def tarefa_em_segundo_plano():
    print("Tarefa em segundo plano iniciando...")
    time.sleep(5)
    print("Tarefa em segundo plano finalizada.")

if __name__ == "__main__":
    processo = multiprocessing.Process(target=tarefa_em_segundo_plano)
    processo.start()

    print("Programa principal continua executando outras tarefas.")
    for _ in range(10):
        print("...")
        time.sleep(1)

    processo.join()
