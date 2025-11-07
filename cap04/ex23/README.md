# Exercício 4.23 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie dois objetos `datetime`, um representando o dia 1 de janeiro de 2022 e outro representando o dia 1 de fevereiro de 2022. Calcule e mostre a diferença entre essas duas datas em dias.

## Solução

```python
import datetime

data1 = datetime.date(2022, 1, 1)
data2 = datetime.date(2022, 2, 1)

diferenca = data2 - data1

print(diferenca.days)
```

## Explicação

Neste código, importamos o módulo `datetime` e criamos dois objetos `date` que representam o dia 1 de janeiro de 2022 e o dia 1 de fevereiro de 2022, respectivamente. Calculamos a diferença entre essas duas datas subtraindo os objetos `date` e, em seguida, acessamos o número de dias da diferença usando o atributo `days` do objeto `timedelta` resultante. Ao fim, o número de dias é impresso.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
