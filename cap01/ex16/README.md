# Exercício 1.16 - Fundamentos da Linguagem

## Enunciado

(**Difícil**) Crie um programa que peça ao usuário para digitar a massa e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.

## Solução

```python
massa = float(input("Digite a massa do objeto: "))
aceleracao = float(input("Digite a aceleração do objeto: "))

forca_resultante = massa * aceleracao

print(f"Força resultante: {forca_resultante:.2f} N")
```

## Explicação

O código utiliza a função `input()` para solicitar que o usuário digite a massa e a aceleração de um objeto, que são armazenados nas variáveis `massa` e `aceleracao`, respectivamente. Em seguida, é calculada a força resultante que atua sobre o objeto, utilizando a fórmula massa * aceleração e impressa utilizando o `print()`. O resultado é formatado com 2 casas decimais e a unidade de medida da força (Newton - N) é especificada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
