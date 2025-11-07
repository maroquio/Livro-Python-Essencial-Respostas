# Exercício 4.8 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase com 5 palavras. Caso a frase digitada tenha uma quantidade diferente de palavras, o usuário deve digitar novamente. Ao fim, mostre uma palavra por linha. Use expressões regulares para extrair as palavras.

## Solução

```python
import re

while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = re.findall(r'b\w+\b', frase)

    if len(palavras) == 5:
        break
    else:
        print("Erro: a frase deve conter exatamente 5 palavras. Tente novamente.")

for palavra in palavras:
    print(palavra)
```

## Explicação

O programa começa importando o módulo `re` para usar expressões regulares. Em seguida, entra em um laço contínuo que pede ao usuário para inserir uma frase. A função `re.findall` é utilizada para encontrar todas as palavras na frase, seguindo a expressão regular `"`` b w+ b``"`, que identifica palavras isoladas. Se a quantidade de palavras (`len(palavras)`) encontradas for igual a 5, o laço é interrompido, indicando que a entrada do usuário é válida. Caso contrário, exibe uma mensagem de erro e solicita uma nova entrada. Por fim, o programa percorre a lista de palavras válidas, imprimindo cada uma em uma linha separada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
