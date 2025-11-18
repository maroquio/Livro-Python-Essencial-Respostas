# Exercício 4.19 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `datetime` representando o dia 15 de janeiro de 2022 às 12:00.

## Solução

```python
import datetime

data_e_hora = datetime.datetime(2022, 1, 15, 12, 0)
print(data_e_hora)
```

## Explicação

Neste código, importamos o módulo `datetime`. Criamos um objeto `datetime` que representa a data e a hora especificadas (15 de janeiro de 2022 às 12:00) passando os valores correspondentes ao construtor `datetime`. No fim, a data e a hora são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
