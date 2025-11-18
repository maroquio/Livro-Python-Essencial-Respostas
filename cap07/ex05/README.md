# Exercício 7.5 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um arquivo vazio qualquer. Agora, na mesma pasta, crie um programa que solicite ao usuário que digite o nome desse arquivo e exclua-o.

## Solução

```python
import os
nome_arquivo = input("Digite o nome do arquivo: ")
os.remove(nome_arquivo)
```

## Explicação

Este programa também utiliza o módulo `os`. Depois de obter o nome do arquivo do usuário, a função `os.remove` é usada para excluir o arquivo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
