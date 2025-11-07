# Exercício 4.29 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `datetime` que represente o instante atual. Em seguida, formate esse instante para exibir o número do dia do ano entre 1 e 365 (ou 366 para anos bissextos).

## Solução

```python
from datetime import datetime

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Formata a data e hora para exibir o número do dia do ano
numero_dia_ano = data_hora_atual.strftime("%j")

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"O número do dia do ano é: {numero_dia_ano}")
```

## Explicação

Nesta solução, inicialmente definimos a data e a hora atuais utilizando a função `datetime.now()`, que são atribuídas à variável `data_hora_atual`. Em seguida, formatamos essa data e hora para exibir o número do dia do ano, usando o método `strftime` com o código de formato `"%j"`, que é atribuído à variável `numero_dia_ano`. Por fim, imprimimos a data e a hora atuais e o número do dia do ano.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
