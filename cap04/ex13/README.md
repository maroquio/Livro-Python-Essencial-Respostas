# Exercício 4.13 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase, divida-a em palavras, remova todos os espaços em branco desnecessários dessas palavras, e componha a frase novamente com apenas 1 espaço entre as palavras.

## Solução

```python
frase = input("Digite uma frase: ")
palavras = frase.split()
nova_frase = ' '.join(palavras)
print(nova_frase)
```

## Explicação

Neste código, o usuário é solicitado a inserir uma frase. Essa frase é dividida em palavras com o método `split()`, que remove todos os espaços em branco. As palavras são então unidas novamente em uma única *string* com um espaço entre cada palavra usando o método `join()`. A frase resultante é impressa.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
