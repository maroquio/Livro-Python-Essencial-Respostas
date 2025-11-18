# Exercício 1.17 - Fundamentos da Linguagem

## Enunciado

Crie um programa que peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma velocidade para a outra. Em seguida, o programa deve calcular e mostrar a aceleração.

## Solução

```python
v_inicial = float(input("Digite a velocidade inicial: "))
v_final = float(input("Digite a velocidade final: "))
tempo = float(input("Digite o tempo de transição (em segundos): "))

aceleracao = (v_final - v_inicial) / tempo

print(f"Aceleração: {aceleracao:.2f} m/s²")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite a velocidade inicial, a velocidade final e o tempo de transição de uma para outra, que são armazenados nas variáveis `v_inicial`, `v_final` e `tempo`, respectivamente. Em seguida, é calculada a aceleração do objeto, utilizando a fórmula (velocidade final - velocidade inicial) / tempo e impressa utilizando o `print()`. O resultado é formatado com 2 casas decimais e a unidade de medida da aceleração (metro por segundo ao quadrado - m/s²) é especificada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
