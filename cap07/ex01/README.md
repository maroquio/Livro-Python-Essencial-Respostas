# Exercício 7.1 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que solicite ao usuário um nome de arquivo e exiba seu conteúdo na tela.

## Solução

```python
nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
```

## Explicação

O programa acima solicita ao usuário que insira o nome do arquivo. Em seguida, ele usa a função `open` para abrir o arquivo em modo de leitura ("r"). O conteúdo do arquivo é lido usando o método `read` e então é impresso na tela.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
