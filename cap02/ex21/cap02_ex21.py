# Capítulo 2 - Exercício 21
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

cor_semaforo = input("Insira a cor atual do semáforo (verde, amarelo, vermelho): ").lower()

match cor_semaforo:
    case "verde":
        print("Prossiga")
    case "amarelo":
        print("Prepare-se para parar")
    case "vermelho":
        print("Pare")
    case _:
        print("Cor inválida")
