# Exercício 4.20 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que mostre a data atual no formato "DD-MM-AAAA".

## Solução

```python
import datetime

data_atual = datetime.date.today()
data_formatada = data_atual.strftime("%d-%m-%Y")
print(data_formatada)
```

## Explicação

Neste código, importamos o módulo `datetime`. Criamos um objeto `date` que representa a data atual usando o método `date.today()`. Formata-se a data no formato "DD-MM-AAAA" usando o método `strftime()` e a string de formatação `"%d-\%m-\%Y"`. Ao fim, a data formatada é impressa.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
