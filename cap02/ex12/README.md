# Exercício 2.12 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se uma pessoa é elegível para aposentadoria (se tem 60 anos ou mais para mulheres e 65 anos ou mais para homens). O usuário deve digitar a idade e o gênero da pessoa a ser verificada.

## Solução

```python
idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (M: masculino, F: feminino): ")

if (genero.upper() == "F" and idade >= 60) or (genero.upper() == "M" and idade >= 65):
    print("Elegível para aposentadoria.")
else:
    print("Não elegível para aposentadoria.")
```

## Explicação

Neste código, solicitamos ao usuário que digite sua idade e gênero, armazenando-os nas variáveis `idade` e `genero`. Usamos a estrutura condicional `if` para verificar se a pessoa é elegível para aposentadoria com base em seu gênero e idade. Se o gênero for "F" e a idade for maior ou igual a 60, ou se o gênero for "M" e a idade for maior ou igual a 65, a pessoa é elegível para aposentadoria e imprimimos a mensagem correspondente. Caso contrário, a pessoa não é elegível para aposentadoria e imprimimos "Não elegível para aposentadoria".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
