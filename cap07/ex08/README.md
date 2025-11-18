# Exercício 7.8 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um programa que exclua o diretório criado no exercício anterior com todo o seu conteúdo (cuidado para não excluir a pasta errada).

## Solução

```python
import shutil
shutil.rmtree("temp")
```

## Explicação

Para este exercício, usamos a função `shutil.rmtree` que remove um diretório inteiro e tudo o que está dentro dele. Como no exercício anterior criamos o diretório "temp", agora excluímos o mesmo.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
