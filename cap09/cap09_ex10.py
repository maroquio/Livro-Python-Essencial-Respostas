# Capítulo 9 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
