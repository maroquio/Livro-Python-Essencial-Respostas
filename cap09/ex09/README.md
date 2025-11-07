# Exercício 9.9 - Tratamento de Exceções

## Enunciado

Crie uma função chamada `read_file` que recebe o nome de um arquivo como argumento e imprime o conteúdo do arquivo. A função deve abrir o arquivo para leitura no bloco `try`, tratar exceções no bloco `except` para o caso do arquivo não existir, e finalmente fechar o arquivo no bloco `finally`, independente de exceções terem sido lançadas ou não.

## Solução

```python
def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        print(arquivo.read())
        arquivo.close()
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    finally:        
        print("Operação finalizada.")

ler_arquivo("exemplo.txt")
```

## Explicação

Esta função chamada `ler_arquivo` recebe o nome de um arquivo como argumento. Dentro do bloco `try`, tentamos abrir o arquivo para leitura e imprimimos o seu conteúdo. Se o arquivo não for encontrado, o Python lançará uma exceção do tipo `FileNotFoundError`. Caso a leitura seja bem sucedida, o arquivo é fechado logo em seguida. No bloco `except`, nós tratamos essa exceção imprimindo uma mensagem para o usuário indicando que o arquivo não foi encontrado. No bloco `finally`, que será executado independentemente de uma exceção ter sido lançada ou não, simplesmente imprimimos a mensagem "Operação finalizada".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
