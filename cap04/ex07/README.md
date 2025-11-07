# Exercício 4.7 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar um nome de usuário e uma senha contendo apenas caracteres alfanuméricos e use uma expressão regular para fazer uma limpeza nos valores digitados, exibindo novamente para o usuário os valores processados.

## Solução

```python
import re

usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

usuario_limpo = re.sub('W+','', usuario )
senha_limpa = re.sub('W+','', senha )

if usuario != usuario_limpo:
    print(f"O nome de usuário foi modificado para: {usuario_limpo}")

if senha != senha_limpa:
    print(f"A senha foi modificada para: {senha_limpa}")
```

## Explicação

Nesta solução, o usuário é solicitado a digitar um nome de usuário e uma senha. A biblioteca `re` é usada para limpar os valores digitados pelo usuário de quaisquer caracteres que não sejam alfanuméricos. Isso é feito usando a função `re.sub()`, que substitui todos os caracteres não alfanuméricos (indicados pelo `' W+'`) por uma *string* vazia. Se o nome de usuário ou senha forem alterados durante o processo de limpeza, eles são impressos na tela.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
