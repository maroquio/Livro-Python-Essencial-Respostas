# Exercício 2.11 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se uma pessoa pode votar ou não, considerando sua idade e sua nacionalidade, digitadas pelo usuário (se tem 16 anos ou mais e é brasileiro, pode votar).

## Solução

```python
idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: ")

if idade >= 16 and nacionalidade.lower() == "brasileira":
    print("Você pode votar.")
else:
    print("Você não pode votar.")
```

## Explicação

Neste código, pedimos ao usuário que digite sua idade e nacionalidade, armazenando esses valores nas variáveis `idade` e `nacionalidade`, respectivamente. Usamos a estrutura condicional `if` para verificar se a idade é maior ou igual a 16 e se a nacionalidade, convertida para letras minúsculas, é igual a "brasileira". Se ambas as condições forem verdadeiras, a pessoa pode votar e imprimimos a mensagem correspondente. Caso contrário, a pessoa não pode votar e imprimimos a mensagem "Você não pode votar".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
