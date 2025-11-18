# Exercício 10.13 - Programação Concorrente

## Enunciado

Escreva um programa Python que utilize `asyncio` e a biblioteca `aiohttp` para baixar vários arquivos da internet de forma assíncrona.

## Solução

```python
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
```

## Explicação

Nesta solução, estamos usando `asyncio` e `aiohttp` para baixar 10 imagens da Internet de forma assíncrona. Para cada tupla (URL, nome do arquivo), criamos uma tarefa para baixar o arquivo e adicionamos essa tarefa à lista de tarefas. Em seguida, usamos `asyncio.gather` para executar todas as tarefas simultaneamente e esperar até que todas elas estejam concluídas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
