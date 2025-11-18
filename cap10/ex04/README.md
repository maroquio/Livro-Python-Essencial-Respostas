# Exercício 10.4 - Programação Concorrente

## Enunciado

Escreva um programa Python que utilize `multiprocessing` para calcular o fatorial de um número. O número deve ser dividido entre dois processos e o resultado final deve ser o fatorial do número. Teste com números a partir de 1000, aumentando em passos de 200 a cada execução.

## Solução

```python
import multiprocessing

def fatorial(n, retorno):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    retorno.put(fatorial)

if __name__ == "__main__":
    num = 10
    metade = num // 2

    retorno1 = multiprocessing.Queue()
    retorno2 = multiprocessing.Queue()

    processo1 = multiprocessing.Process(target=fatorial, args=(metade, retorno1))
    processo2 = multiprocessing.Process(target=fatorial, args=(num - metade, retorno2))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

    resultado_final = retorno1.get() * retorno2.get()
    print(f"O fatorial de {num} é {resultado_final}")
```

## Explicação

Nesta solução, estamos calculando o fatorial de um número utilizando o módulo `multiprocessing`. Dividimos o número ao meio e cada processo calcula o fatorial de uma metade. O fatorial do número inteiro é obtido multiplicando os resultados dos dois processos. Usamos `Queues` para retornar os resultados dos processos para o processo principal.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
