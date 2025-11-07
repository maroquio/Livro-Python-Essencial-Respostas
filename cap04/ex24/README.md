# Exercício 4.24 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie dois objetos `datetime`, um representando as 8:00h da manhã e outro representando as 3:00h da tarde do mesmo dia. Calcule a diferença entre esses dois horários em horas.

## Solução

```python
import datetime

hora1 = datetime.datetime.strptime("08:00", "%H:%M")
hora2 = datetime.datetime.strptime("15:00", "%H:%M")

diferenca = hora2 - hora1

print(diferenca.seconds / 3600)
```

## Explicação

Neste código, importamos o módulo `datetime`. Criamos dois objetos `datetime` que representam as 8:00 da manhã e as 3:00 da tarde, respectivamente, usando `datetime.strptime()`. Em seguida, calculamos a diferença entre esses dois horários subtraindo os objetos `datetime` e acessamos o número de segundos da diferença usando o atributo `seconds` do objeto `timedelta` resultante. Para obter a diferença em horas, dividimos o número de segundos por 3600. O número de horas é impresso ao final.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
