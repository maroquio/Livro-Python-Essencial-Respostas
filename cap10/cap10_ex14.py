# Capítulo 10 - Exercício 14
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

import asyncio

async def tarefa_demorada():
    print("Iniciando tarefa demorada...")
    for i in range(5):
        await asyncio.sleep(5)
        print(f"Etapa {i+1} da tarefa demorada concluída")

async def main():
    asyncio.create_task(tarefa_demorada())    

    for i in range(10):
        print(f"Tarefa do programa principal {i+1}")
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
