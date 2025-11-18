# Exercício 10.1 - Programação Concorrente

## Enunciado

Escreva um programa Python que utilize `multiprocessing` para calcular a soma de uma lista contendo 99.999.999 números inteiros. A lista deve ser dividida entre dois processos e o resultado final deve ser a soma total dos números. Ao fim, o programa deve exibir a soma e o tempo de execução.

## Solução

```python
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
```

## Explicação

Nesta solução, estamos usando o módulo `multiprocessing` para dividir uma lista de números em duas metades e somar os números em cada metade em dois processos separados. Usamos uma `Queue` para cada processo para retornar o resultado da soma para o processo principal, que então soma os resultados dos dois processos para obter a soma total dos números.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
