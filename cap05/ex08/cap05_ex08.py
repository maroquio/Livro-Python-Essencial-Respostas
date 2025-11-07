# Capítulo 5 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

def decifrar_mensagem(mensagem):
    if len(mensagem) == 0:
        return mensagem
    else:
        char_decifrado = chr((ord(mensagem[0]) - 98) % 26 + 97)
        return char_decifrado + decifrar_mensagem(mensagem[1:])

print(decifrar_mensagem('bdfn'))  
# Saída: 'acem'
