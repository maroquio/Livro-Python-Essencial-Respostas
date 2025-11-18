# Exercício 1.21 - Fundamentos da Linguagem

## Enunciado

(**Difícil**) Crie um programa que peça ao usuário para digitar a distância percorrida, o tempo gasto e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a velocidade inicial e final.

## Solução

```python
distancia = float(input("Digite a distância percorrida (m): "))
tempo = float(input("Digite o tempo gasto (s): "))
aceleracao = float(input("Digite a aceleração (m/s²): "))

v_inicial = (distancia - 0.5 * aceleracao * tempo**2) / tempo
v_final = v_inicial + aceleracao * tempo

print(f"Velocidade inicial: {v_inicial:.2f} m/s")
print(f"Velocidade final: {v_final:.2f} m/s")
```

## Explicação

Neste código, primeiro solicitamos ao usuário a distância percorrida, o tempo gasto e a aceleração, e armazenamos os valores nas variáveis `distancia`, `tempo` e `aceleracao`, respectivamente. Em seguida, calculamos a velocidade inicial utilizando a fórmula `v_inicial = (distancia - 0.5 * aceleracao * tempo**2) / tempo` e a velocidade final com `v_final = ``v_inicial`` + aceleracao * tempo`. Por fim, imprimimos os resultados formatados com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
