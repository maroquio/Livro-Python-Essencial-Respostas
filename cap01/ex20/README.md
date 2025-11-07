# Exercício 1.20 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o programa deve calcular e mostrar a velocidade média do objeto.

## Solução

```python
distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo gasto (em horas): "))

velocidade_media = distancia / tempo

print(f"A velocidade média é: {velocidade_media:.2f} km/h")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite a distância percorrida por um objeto e o tempo gasto no trajeto, que são armazenados nas variáveis `distancia` e `tempo`, respectivamente. Em seguida, é calculada a velocidade média do objeto, utilizando a fórmula velocidade média = distância / tempo e impressa utilizando o `print()`. O resultado é formatado com 2 casas decimais e a unidade de medida da velocidade (quilômetros por hora - km/h) é especificada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
