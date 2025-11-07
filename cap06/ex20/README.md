# Exercício 6.20 - Coleções

## Enunciado

Faça um programa que leia continuamente o número da camisa (chave) e o nome (valor) de jogadores de futebol, armazenando os dados em um dicionário. O programa deve ler até que o usuário digite -1 no número da camisa. Ao fim, o programa deve mostrar os jogadores ordenados pelo número da camisa.

## Solução

```python
jogadores = {}
while True:
    numero = int(input("Digite o número da camisa: "))
    if numero == -1:
        break
    nome = input("Digite o nome do jogador: ")
    jogadores[numero] = nome

for numero, nome in sorted(jogadores.items()):
    print(f"Camisa {numero}: {nome}")
```

## Explicação

Neste programa, inicialmente, é criado um dicionário vazio chamado `jogadores`. Em seguida, é usado um laço `while True`, que executará indefinidamente até que seja interrompido por um comando `break`. Dentro deste laço, o programa pede ao usuário que insira o número da camisa do jogador (que é convertido para um número inteiro usando a função `int()`). Se o número da camisa for -1, o laço é interrompido. Se não, o programa pede ao usuário que insira o nome do jogador. O número da camisa e o nome do jogador são então adicionados ao dicionário `jogadores`. Após a conclusão do laço (ou seja, quando o usuário insere -1 para o número da camisa), o programa percorre os itens do dicionário `jogadores` em ordem (ordenado pelo número da camisa, pois é a chave do dicionário). Para cada item, ele imprime o número da camisa e o nome do jogador. A função `sorted()` é usada para classificar os itens do dicionário por chave (ou seja, pelo número da camisa), e o método `items()` é usado para obter uma visualização dos pares de chave-valor no dicionário.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
