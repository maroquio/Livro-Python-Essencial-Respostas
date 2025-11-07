# Exercício 2.9 - Estruturas Condicionais

## Enunciado

Crie um programa que calcule a média de três números e exiba a mensagem "Aprovado" se a média for maior ou igual a 6 ou "Reprovado" caso contrário. Se a nota for 10, exiba também a mensagem "Parabéns".

## Solução

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado")
    if media == 10:
        print("Parabéns")
else:
    print("Reprovado")
```

## Explicação

Neste código, solicitamos ao usuário que digite três notas e as convertemos para `float` antes de armazená-las nas variáveis `nota1`, `nota2` e `nota3`. Calculamos a média das notas somando-as e dividindo o resultado por 3, armazenando-o na variável `media`. Usamos a estrutura condicional `if` para verificar se a média é maior ou igual a 6. Se for, o aluno está "Aprovado" e imprimimos a mensagem. Se a média for igual a 10, também imprimimos a mensagem "Parabéns". Caso contrário, o aluno está "Reprovado" e imprimimos a mensagem correspondente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
