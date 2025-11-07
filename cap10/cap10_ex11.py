# Capítulo 10 - Exercício 11
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
