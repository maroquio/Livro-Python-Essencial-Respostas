# Exercício 9.5 - Tratamento de Exceções

## Enunciado

Crie uma função que leia um arquivo de texto e exiba o conteúdo na tela. Trate exceções caso o arquivo não exista ou não seja possível lê-lo.

## Solução

```python
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IOError:
        print("Erro: Não foi possível ler o arquivo.")

ler_arquivo("arquivo_inexistente.txt")
```

## Explicação

A função `ler_arquivo` tenta abrir um arquivo com o nome fornecido no modo de leitura. Se o arquivo não existir, será lançada uma `FileNotFoundError`, que é capturada e tratada com uma mensagem de erro apropriada. Se houver algum problema ao ler o arquivo (por exemplo, se não tivermos permissão para ler o arquivo), uma `IOError` será lançada, que também é capturada e tratada com uma mensagem de erro apropriada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
