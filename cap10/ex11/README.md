# Exercício 10.11 - Programação Concorrente

## Enunciado

Escreva um programa Python que utilize `asyncio` para fazer solicitações HTTP de forma assíncrona a 3 URLs de sites de sua preferência usando `await` em cada solicitação, computando o tempo de execução.

## Solução

```python
import asyncio
from time import perf_counter
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['https://python.org', 
        'https://maroquio.com',
        'https://youtube.com/maroquio']
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(html)

if __name__ == '__main__':    
    inicio = perf_counter()
    asyncio.run(main())
    fim = perf_counter()
    print(f'Tempo de execução: {fim - inicio:.2f} segundos.')
```

## Explicação

Nesta solução, estamos usando `asyncio` e `aiohttp` para fazer uma solicitação HTTP de forma assíncrona. Criamos uma função `fetch` que recebe um objeto de sessão e uma URL e retorna o texto da resposta HTTP. A função `main` cria uma sessão e, para cada URL da lista, busca o conteúdo da URL especificada usando `await` e imprime o resultado, de forma sequencial.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
