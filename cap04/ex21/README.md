# Exercício 4.21 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que formate a hora atual no formato de 12 horas, incluindo AM/PM.

## Solução

```python
import datetime

hora_atual = datetime.datetime.now()
hora_formatada = hora_atual.strftime("%I:%M %p")
print(hora_formatada)
```

## Explicação

Neste código, importamos o módulo `datetime` e obtemos a data e hora atuais como um objeto `datetime` usando `datetime.now()`. Em seguida, formatamos a hora no formato de 12 horas, incluindo AM/PM, usando o método `strftime()` e a string de formatação `"%I:\%M \%p"`, "I" representa a hora no formato 12 horas, "M" representa os minutos e "p" representa o sufixo "AM" ou "PM". A hora formatada é impressa ao final.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
