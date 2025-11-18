# Exercício 10.12 - Programação Concorrente

## Enunciado

Modifique o programa anterior para que as solicitações HTTP sejam feitas em paralelo utilizando a função `asyncio.gather` e compare o tempo de execução com a solução do exercício anterior.

## Solução

```python
import asyncio
from time import perf_counter
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        urls = ['https://python.org', 
            'https://maroquio.com',
            'https://youtube.com/maroquio']
        for url in urls:
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

if __name__ == '__main__':    
    inicio = perf_counter()
    asyncio.run(main())
    fim = perf_counter()
    print(f'Tempo de execução: {fim - inicio:.2f} segundos.')
```

## Explicação

Nesta solução, estamos usando `asyncio.gather` para fazer várias solicitações HTTP ao mesmo tempo. Para cada URL, criamos uma tarefa de busca e adicionamos essa tarefa à lista de tarefas. Depois, usamos `asyncio.gather` para executar todas as tarefas simultaneamente e esperar até que todas elas estejam concluídas. Como se trata de um problema com gargalo do tipo *I/O Bound*, o tempo de execução se torna menor, ainda que tudo seja executado em um único processo e núcleo de computação.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
