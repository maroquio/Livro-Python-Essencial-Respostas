# Exercício 7.2 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que leia um arquivo texto e exiba quantas linhas ele possui.

## Solução

```python
nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
print(len(linhas))
```

## Explicação

Neste programa, depois de abrir o arquivo, utilizamos o método `readlines` para ler todas as linhas do arquivo e armazená-las na lista `linhas`. Então, a função `len` é usada para obter o número de linhas no arquivo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
