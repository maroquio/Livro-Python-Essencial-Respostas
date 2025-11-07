# Capítulo 2 - Exercício 8
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

texto = input("Digite uma data (dd/mm/aaaa): ")

if len(texto) == 10 and texto[2] == '/' and texto[5] == '/':
    dia = int(texto[:2])
    mes = int(texto[3:5])
    ano = int(texto[6:])

    if (1 <= dia <= 31) and (1 <= mes <= 12) and (1 <= ano <= 9999):
        print("Data válida no formato 'dd/mm/aaaa'.")
    else:
        print("Data inválida no formato 'dd/mm/aaaa'.")
else:
    print("O texto não corresponde a uma data.")
