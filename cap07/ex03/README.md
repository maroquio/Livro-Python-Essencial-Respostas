# Exercício 7.3 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que leia um arquivo texto, inverta o conteúdo de cada linha e salve o resultado em um novo arquivo.

## Solução

```python
nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

linhas_invertidas = [linha[::-1] for linha in linhas]

with open("arquivo_invertido.txt", "w") as arquivo:
    arquivo.writelines(linhas_invertidas)
```

## Explicação

Neste código, as linhas do arquivo são invertidas usando a notação de slice [::-1] e armazenadas na lista `linhas_invertidas`. Em seguida, um novo arquivo chamado "arquivo_invertido.txt" é criado em modo de escrita ("w") e as linhas invertidas são escritas nele usando o método `writelines`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
