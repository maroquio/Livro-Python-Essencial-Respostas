# Exercício 10.14 - Programação Concorrente

## Enunciado

Crie um programa que use `asyncio` para realizar uma tarefa demorada em segundo plano, executando 5 etapas de 5 segundos cada, enquanto o programa principal continua executando 10 tarefas de 1 segundo cada.

## Solução

```python
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
```

## Explicação

No código acima, a função `tarefa_demorada` simula uma tarefa que leva um longo tempo para ser concluída, composta por 5 etapas de 5 segundos cada. No laço principal, chamamos `asyncio.create_task` para iniciar a tarefa longa em um novo objeto `task`, permitindo que o programa principal continue realizando suas próprias tarefas. Observe que, diferentemente do que acontece com a técnica *multithreading*, o programa principal não aguarda o término da tarefa demorada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
