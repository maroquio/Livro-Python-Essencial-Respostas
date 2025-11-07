# Capítulo 10 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import threading
import time

def tarefa_demorada():
    print("Iniciando tarefa demorada...")
    for i in range(5):
        time.sleep(5)
        print(f"Etapa {i+1} da tarefa demorada concluída")

if __name__ == "__main__":
    threading.Thread(target=tarefa_demorada).start()

    for i in range(10):
        print(f"Tarefa do programa principal {i+1}")
        time.sleep(1)
