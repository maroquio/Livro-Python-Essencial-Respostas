# Capítulo 10 - Exercício 15
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import asyncio
import aiohttp

async def get_response(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        url = 'https://www.boredapi.com/api/activity'
        for _ in range(10):
            tasks.append(get_response(session, url))
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

if __name__ == '__main__':
    asyncio.run(main())
