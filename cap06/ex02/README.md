# Exercício 6.2 - Coleções

## Enunciado

Faça um programa que use *List Comprehension* para criar uma lista com as palavras que contêm a letra "a" em uma frase digitada pelo usuário, substituindo a letra por "o".

## Solução

```python
# Solicita ao usuário para digitar uma frase
frase = input("Digite uma frase: ")

# Cria uma lista com as palavras que contêm a letra "a", substituindo a letra por "o"
palavras_modificadas = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]

print(palavras_modificadas)
```

## Explicação

Nesta solução, pedimos ao usuário para digitar uma frase. Em seguida, usamos *list comprehension* para gerar uma lista de palavras que contêm a letra "a", substituindo "a" por "o". A função `split()` divide a frase em palavras e a condição `"a" in palavra` garante que apenas as palavras que contêm a letra "a" sejam selecionadas. A função `replace("a", "o")` substitui todas as ocorrências de "a" por "o" em cada palavra selecionada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
