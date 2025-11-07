# Capítulo 9 - Exercício 9
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
