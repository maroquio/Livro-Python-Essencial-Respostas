# Exercício 9.10 - Tratamento de Exceções

## Enunciado

Crie uma função chamada `importar_modulo` que recebe o nome de um módulo como argumento e tenta importá-lo. A função deve usar um bloco para tratar a exceção `ModuleNotFoundError` caso o módulo não exista. Se a importação for bem sucedida, a função deve imprimir uma mensagem dizendo que o módulo foi importado com sucesso. Caso contrário, deve imprimir uma mensagem informando que o módulo não foi encontrado. Independentemente de ocorrer ou não uma exceção, a função deve imprimir "Operação finalizada." ao final.

## Solução

```python
def importar_modulo(modulo):
    try:
        __import__(modulo)
        print(f"O módulo {modulo} foi importado com sucesso.")
    except ModuleNotFoundError:
        print(f"O módulo {modulo} não foi encontrado.")
    finally:
        print("Operação finalizada.")

# Exemplo de uso da função para importar a biblioteca numpy
importar_modulo("numpy")
```

## Explicação

Esta função, chamada `importar_modulo`, recebe o nome de um módulo como argumento. No bloco `try`, tentamos importar o módulo usando a função *built-in* `__import__()`, que recebe o nome do módulo como uma *string* e tenta importá-lo. Se a importação for bem-sucedida, imprimimos uma mensagem informando que o módulo foi importado com sucesso. Se o módulo não existir, o Python lançará uma exceção `ModuleNotFoundError`. No bloco `except`, tratamos essa exceção imprimindo uma mensagem informando que o módulo não foi encontrado. No bloco `finally`, que será executado independentemente de uma exceção ter sido lançada ou não, imprimimos a mensagem "Operação finalizada.".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
