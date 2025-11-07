# Exercício 4.22 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que formate o instante atual para mostrá-las no formato "terça-feira, 13 de junho de 2023, 19:22.".

## Solução

```python
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%A, %d de %B de %Y, %H:%M")

print(data_formatada)
```

## Explicação

Neste código, importamos os módulos `datetime` e `locale`. Configuramos o idioma para português brasileiro usando `locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')`. Em seguida, obtemos a data e hora atuais como um objeto `datetime` usando `datetime.now()` e formatamos a data e hora para incluir o nome do dia da semana e do mês em português usando o método `strftime()` e a string de formatação `"%A, \%d de \%B de \%Y, \%H:\%M"`. As constantes de formatação "A" e "B" representam, respectivamente, os nomes do dia da semana e do mês. A data e hora formatadas são impressas ao final.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
