# Exercício 4.28 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie dois objetos `datetime`, um representando o instante atual e outro representando um instante no futuro. Verifique se o instante atual é realmente anterior ao instante futuro.

## Solução

```python
from datetime import datetime, timedelta

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Define uma data e hora futura
data_hora_futura = datetime(2025, 1, 1, 10, 30)

# Verifica se a data e hora atuais são anteriores à data e hora futura
eh_antes = data_hora_atual < data_hora_futura

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"A data e hora futura são: {data_hora_futura}")
print(f"A data e hora atuais são anteriores à data e hora futura? {eh_antes}")
```

## Explicação

Nesta solução, inicialmente definimos a data e a hora atuais utilizando a função `datetime.now()`, que são atribuídas à variável `data_hora_atual`. Em seguida, definimos uma data e hora futura inicializando um objeto `datetime` com uma data e hora específicas, que são atribuídas à variável `data_hora_futura`. A operação de comparação "$<$" é usada para verificar se a data e hora atuais são anteriores à data e hora futura. O resultado é um valor booleano que é atribuído à variável `eh_antes`. Finalmente, as duas datas e horas e o resultado da comparação são impressos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
