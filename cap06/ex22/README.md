# Exercício 6.22 - Coleções

## Enunciado

Considere uma *string* que contém todas as letras do alfabeto. Escreva um programa em Python que use a função `random.choice` para escolher continuamente uma letra até que todas as letras do seu nome tenham sido sorteadas. Ao fim, mostre a quantidade de sorteios que foram realizados até a obtenção de todas as letras de seu nome.

## Solução

```python
import random
letras = 'abcdefghijklmnopqrstuvwxyz'
nome = 'maroquio'
letras_nome = set(nome)
sorteios = 0
letras_sorteadas = ''

while set(letras_sorteadas) != set(letras_nome):
    letra = random.choice(letras)
    if letra in letras_nome and letra not in letras_sorteadas:
        letras_sorteadas += letra
    sorteios += 1

print(nome, letras_sorteadas)
print(sorteios)
```

## Explicação

Este programa começa importando o módulo `random` do Python. A variável `letras` é uma *string* contendo todas as letras minúsculas do alfabeto. A variável `nome` é uma *string* contendo o nome de interesse. O nome é então convertido para um conjunto para eliminar duplicatas. O quantificador `sorteios` é inicializado em 0 e `letras_sorteadas` é uma *string* vazia que armazena as letras sorteadas que estão no nome. O programa então entra em um laço `while`, que continua sorteando letras até que todas as letras do nome tenham sido sorteadas. Se a letra sorteada estiver no nome e ainda não tiver sido sorteada, ela é adicionada a `letras_sorteadas`. A contagem de `sorteios` é incrementada a cada iteração, independentemente do resultado do sorteio. Finalmente, o programa imprime o número total de sorteios necessários para sortear todas as letras do nome.

Perceba que o tipo de dados "conjunto" (`set`) foi usado para comparar as letras do nome com as letras sorteadas. Um conjunto é uma coleção não ordenada de itens únicos, o que o torna ideal para este propósito, pois ignora a ordem e as repetições das letras.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
