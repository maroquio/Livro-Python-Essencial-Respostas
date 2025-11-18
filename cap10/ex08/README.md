# Exercício 10.8 - Programação Concorrente

## Enunciado

Escreva um programa que utilize o módulo `multithreading` para criar 10 *threads* que receba e exiba um números de 1 a 10, sendo que cada *thread* deve ter um atraso aleatório entre 1 e 4 segundos.

## Solução

```python
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
```

## Explicação

Esta solução cria 10 *threads*, sendo que cada uma delas exibe um número de 1 a 10 após um atraso aleatório entre 1 e 4 segundos. A função `mostrar_numero` é definida para simular o atraso e exibir o número. A função `random.randint` é usada para gerar um tempo aleatório. No programa principal, 10 instâncias da classe `threading.Thread` são criadas e iniciadas, cada uma com um número de índice entre 1 e 10 como argumento para a função `mostrar_numero`. Quando as *threads* são iniciados, cada uma delas espera pelo atraso gerado aleatoriamente e então exibe o seu número.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
