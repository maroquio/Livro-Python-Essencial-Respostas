# Exercício 4.1 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para inserir dois números e calcule a potência do primeiro número pelo segundo número.

## Solução

```python
# Solicita ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula a potência do primeiro número pelo segundo
potencia = num1 ** num2

# Imprime o resultado
print(f"A potência de {num1} pelo {num2} é {potencia}")
```

## Explicação

Nesta solução, o programa começa solicitando ao usuário que insira dois números, os quais são armazenados nas variáveis `num1` e `num2`. Em seguida, ele calcula a potência do primeiro número pelo segundo usando o operador de potência (`**`) do Python, e armazena o resultado na variável `potencia`. Finalmente, o programa imprime o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
