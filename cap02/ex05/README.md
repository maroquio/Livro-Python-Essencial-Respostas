# Exercício 2.5 - Estruturas Condicionais

## Enunciado

Crie um programa que, a partir da idade digitada pelo usuário, verifique se ele é maior de idade ou não .

## Solução

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

## Explicação

Neste código, solicitamos ao usuário que digite sua idade e armazenamos o valor na variável `idade`. Em seguida, verificamos se o usuário é maior de idade usando a estrutura condicional `if`. Se a idade for maior ou igual a 18, o usuário é considerado maior de idade; caso contrário, é considerado menor de idade. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
