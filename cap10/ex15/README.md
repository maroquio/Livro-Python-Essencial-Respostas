# Exercício 10.15 - Programação Concorrente

## Enunciado

Escreva um programa que use `asyncio` e `aiohttp` para realizar 10 solicitações HTTP para a API *https://www.boredapi.com/api/activity* e imprima as respostas de forma assíncrona. A cada solicitação, esta API retorna um JSON com uma sugestão de atividade para você realizar.

## Solução

```python
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
```

## Explicação

Neste exemplo, estamos usando `asyncio` e `aiohttp` para fazer 10 solicitações HTTP para uma API de forma assíncrona. A cada iteração do laço `for`, criamos uma tarefa para obter a resposta e adicionamos essa tarefa à lista de tarefas. Em seguida, usamos `asyncio.gather` para executar todas as tarefas simultaneamente e esperar até que todas elas estejam concluídas. As respostas das solicitações HTTP são então impressas. Esta é uma maneira eficiente de fazer várias solicitações a uma API de forma assíncrona em Python, o que pode ser particularmente útil quando você precisa coletar muitos dados de uma API em um curto período de tempo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
