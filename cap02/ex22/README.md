# Exercício 2.22 - Estruturas Condicionais

## Enunciado

Crie um programa que solicite ao usuário digitar uma descrição do clima (ensolarado, chuvoso, nublado etc.) e utilize a estrutura `match..case` para imprimir uma sugestão de roupa adequada para o dia (por exemplo, óculos de sol para ensolarado, guarda-chuva para chuvoso etc.).

## Solução

```python
clima = input("Insira a descrição do clima (ensolarado, chuvoso, nublado etc.): ").lower()

match clima:
    case "ensolarado":
        print("Use óculos de sol")
    case "chuvoso":
        print("Leve um guarda-chuva")
    case "nublado":
        print("Leve um casaco leve")
    case _:
        print("Clima não reconhecido")
```

## Explicação

Nesta solução, solicitamos ao usuário uma descrição do clima e usamos a estrutura `match` para sugerir uma roupa ou acessório adequado para o dia. As sugestões são impressas com base na descrição do clima inserida. Um caso padrão é incluído para lidar com entradas não reconhecidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
