# Exercício 2.25 - Estruturas Condicionais

## Enunciado

Crie um programa que peça ao usuário para inserir dois números, *a* e *b*, e uma operação aritmética (+, -, * ou /). Use a estrutura `match..case` para avaliar uma expressão que combine a operação inserida pelo usuário e, em seguida, imprima o resultado da operação escolhida.

## Solução

```python
a = float(input("Insira o número a: "))
b = float(input("Insira o número b: "))
op = input("Insira a operação aritmética (+, -, * ou /): ")
result = None

match op:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        if b != 0:
            result = a / b
        else:
            result = "Divisão por zero não permitida"
    case _:
        result = "Operação inválida"

print(f"Resultado: {result}")
```

## Explicação

Nesta solução, pedi,os ao usuário para inserir dois números, `a` e `b`, e uma operação aritmética `op` (+, -, * ou /). Utilizamos a estrutura `match` para avaliar a operação aritmética inserida pelo usuário e calcular o resultado da operação escolhida. A estrutura `match` é usada para comparar a operação com os quatro casos possíveis e calcular o resultado de acordo. No caso da divisão, é feita uma verificação adicional para garantir que o denominador não seja zero, evitando assim uma divisão por zero. Um caso padrão é incluído para capturar qualquer outra entrada e imprimir "Operação inválida". O resultado da operação é então impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
