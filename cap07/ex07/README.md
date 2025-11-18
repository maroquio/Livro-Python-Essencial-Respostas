# Exercício 7.7 - Arquivos, Módulos e Pacotes

## Enunciado

Faça um programa que crie um diretório chamado "temp" e, dentro desse diretório, crie também um arquivo chamado "temp.txt".

## Solução

```python
import os
os.mkdir("temp")
with open("temp/temp.txt", "w") as arquivo:
    pass
```

## Explicação

Neste programa, usamos o módulo `os` para criar um novo diretório chamado "temp" através da função `os.mkdir`. Em seguida, criamos um arquivo chamado "temp.txt" dentro desse diretório usando a função `open` em modo de escrita ("w"). A palavra-chave `pass` é usada para indicar que não queremos fazer nada dentro do bloco `with`, ou seja, estamos apenas criando um arquivo vazio.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
