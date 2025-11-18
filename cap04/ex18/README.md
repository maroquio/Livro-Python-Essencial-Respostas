# Exercício 4.18 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `time` que represente a hora atual.

## Solução

```python
from datetime import datetime as dt

hora_atual = dt.now().time()
print(hora_atual.strftime("%H:%M:%S"))
```

## Explicação

Nesta solução, importamos a classe `datetime` do módulo `datetime` e a apelidamos de `dt`. Em seguida, criamos a variável `hora_atual` e atribuímos a ela o retorno do método `now()` da classe `datetime`, que contém a data e hora atuais, mas usamos o método `time()` para extrair apenas a parte do horário. Por fim, usamos a função `strftime("%H:\%M:\%S")` para formatar a hora atual no formato de 24 horas e então imprimimos esse resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
