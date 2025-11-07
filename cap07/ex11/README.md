# Exercício 7.11 - Arquivos, Módulos e Pacotes

## Enunciado

Crie um módulo chamado "Utils.py" com uma função chamada `exibir_data_hora`, que simplesmente mostre a data e a hora atuais no terminal. Agora crie um programa que utilize esse módulo personalizado para exibir a data e a hora atuais do sistema.

## Solução

```python
# Conteúdo do arquivo Utils.py
import datetime

def exibir_data_hora():
    print(datetime.datetime.now())

# Programa principal main.py
import Utils

Utils.exibir_data_hora()
```

## Explicação

Neste código, primeiro criamos um arquivo chamado Utils.py com uma função chamada `exibir_data_hora` que imprime a data e a hora atuais usando a classe `datetime` do módulo `datetime`. No programa principal (arquivo main.py), importamos o módulo `Utils` e usamos sua função `exibir_data_hora` para imprimir a data e a hora atuais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
