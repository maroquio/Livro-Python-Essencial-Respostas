# Exercício 10.9 - Programação Concorrente

## Enunciado

Crie um programa que use `multithreading` para realizar uma tarefa demorada em segundo plano, executando 5 etapas de 5 segundos cada, enquanto o programa principal continua executando 10 tarefas de 1 segundo cada.

## Solução

```python
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
```

## Explicação

Nesta solução, criamos uma função chamada `tarefa_demorada` para simular uma tarefa que executa 5 etapas de 5 segundos para finalizar. No processo principal, iniciamos uma `thread` para executar a tarefa demorada, enquanto o próprio processo principal continua executando outras tarefas que demoram 1 segundo cada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
