# Exercício 10.5 - Programação Concorrente

## Enunciado

Crie um programa que use o módulo `multiprocessing` para executar uma tarefa em segundo plano que demora 5 segundos para finalizar enquanto o programa principal continua executando outras 10 tarefas que demoram 1 segundo cada.

## Solução

```python
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
```

## Explicação

Nesta solução, criamos uma tarefa que leva algum tempo para ser concluída e a executamos em um processo separado. Enquanto a tarefa em segundo plano está sendo executada, o programa principal continua executando outras tarefas. A função `time.sleep()` é usada para simular tarefas que levam algum tempo para ser concluídas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
