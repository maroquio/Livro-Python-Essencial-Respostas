# Exercício 2.21 - Estruturas Condicionais

## Enunciado

Crie um programa que simule um semáforo de trânsito. Peça ao usuário para inserir a cor atual do semáforo (verde, amarelo ou vermelho) e utilize a estrutura `match..case` para imprimir uma ação correspondente. Por exemplo, se a cor for verde, imprima "Prossiga"; se for amarelo, imprima "Prepare-se para parar"; se for vermelha, imprima "Pare". Inclua um caso geral que imprima "Cor inválida" para qualquer outra entrada.

## Solução

```python
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
```

## Explicação

Neste código, pedimos ao usuário para inserir a cor atual do semáforo e utilizamos a estrutura `match` para imprimir uma ação correspondente. A cor inserida é convertida para minúsculas para garantir que a comparação seja feita independentemente da capitalização. A estrutura `match` é usada para comparar a cor com os três casos possíveis e imprimir a ação adequada. Um caso padrão usando `_` é incluído para capturar qualquer outra entrada e imprimir "Cor inválida".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
