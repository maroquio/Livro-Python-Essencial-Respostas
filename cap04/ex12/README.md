# Exercício 4.12 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, verifique quantas palavras terminam com a letra "o" e quantas terminam com a letra "a".

## Solução

```python
frase = input("Digite uma frase: ")

palavras = frase.split()
conta_o = sum([1 for palavra in palavras if palavra.endswith('o')])
conta_a = sum([1 for palavra in palavras if palavra.endswith('a')])

print("Palavras terminadas em 'o':", conta_o)
print("Palavras terminadas em 'a':", conta_a)
```

## Explicação

Neste código, o usuário é solicitado a inserir uma frase. A frase é então dividida em palavras usando o método `split()`. Usamos duas *list comprehensions* para contar quantas palavras terminam em "o" e "a", respectivamente, usando o método `endswith()`. Por fim, as contagens resultantes são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
