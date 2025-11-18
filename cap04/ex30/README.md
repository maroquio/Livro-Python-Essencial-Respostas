# Exercício 4.30 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `datetime` representando o instante atual. Em seguida, formate esse instante para exibir o número da semana do ano (de 1 a 52).

## Solução

```python
from datetime import datetime

# Define a data e hora atuais
data_hora_atual = datetime.now()

# Formata a data e hora para exibir o número da semana do ano
numero_semana_ano = data_hora_atual.strftime("%U")

print(f"A data e hora atuais são: {data_hora_atual}")
print(f"O número da semana do ano é: {numero_semana_ano}")
```

## Explicação

Nesta solução, de maneira similar ao exercício anterior, definimos a data e a hora atuais utilizando a função `datetime.now()`, que são atribuídas à variável `data_hora_atual`. A seguir, formatamos essa data e hora para exibir o número da semana do ano, usando o método `strftime` com o código de formato `"%U"`, que é atribuído à variável `numero_semana_ano`. Finalmente, imprimimos a data e a hora atuais e o número da semana do ano.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
