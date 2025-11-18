# Capítulo 9 - Exercício 5
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IOError:
        print("Erro: Não foi possível ler o arquivo.")

ler_arquivo("arquivo_inexistente.txt")
