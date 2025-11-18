# Capítulo 10 - Exercício 13
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import asyncio
import aiohttp

async def download_file(session, url, filename):
    async with session.get(url) as response:
        with open(filename, 'wb') as f:
            f.write(await response.content.read())

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        files = []
        for i in range(1, 10):
            files.append(('https://picsum.photos/2000?random={i}', f'file{i}.jpg'))
        for url, filename in files:
            tasks.append(download_file(session, url, filename))
        await asyncio.gather(*tasks)

if __name__ == '__main__':    
    asyncio.run(main())
