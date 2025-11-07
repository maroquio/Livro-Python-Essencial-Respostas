# Exercício 6.28 - Coleções

## Enunciado

Implemente um *generator* chamado "pega_palavras" que receba um texto e retorne, a cada iteração, uma palavra desse texto (considerando que as palavras são separadas por espaço). Teste seu *generator* com uma frase à sua escolha.

## Solução

```python
def pega_palavras(texto):
    palavras = texto.split(" ")
    for palavra in palavras:
        yield palavra

texto = "Esta é uma frase de exemplo"
generator = pega_palavras(texto)
for palavra in generator:
    print(palavra)
```

## Explicação

A função `pega_palavras` recebe uma *string* como entrada, a divide em palavras individuais (usando espaço como separador) e, em seguida, usa `yield` para retornar cada palavra uma a uma. Por fim, esta função é usada com um laço `for` para imprimir todas as palavras no texto.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
