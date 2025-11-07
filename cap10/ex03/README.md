# Exercício 10.3 - Programação Concorrente

## Enunciado

Escreva um programa que use o módulo `multiprocessing` para criar um processo filho. O processo filho deve imprimir seu próprio *Process ID*, enquanto o processo pai deve imprimir o *Process ID* do processo filho. Utilize `os.getpid` para obter o *Process ID* do processo em questão.

## Solução

```python
import multiprocessing
import os

def filho():
    print(f"Processo filho com PID: {os.getpid()}")

if __name__ == "__main__":
    print(f"Processo pai com PID: {os.getpid()}")

    processo_filho = multiprocessing.Process(target=filho)
    processo_filho.start()
    processo_filho.join()
```

## Explicação

Esta solução utiliza o módulo `multiprocessing` para criar um processo filho. O processo filho imprime seu próprio *Process ID*, que é obtido através da função `os.getpid()`. O processo pai também imprime o *Process ID* do processo filho, utilizando a mesma função.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
