# Exercício 4.27 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `datetime` representando um instante específico. Em seguida, adicione 2 dias e 5 horas a esse instante utilizando `timedelta`.

## Solução

```python
from datetime import datetime, timedelta

# Define uma data e hora específicas
data_hora_especifica = datetime(2023, 1, 1, 10, 30)

# Adiciona 2 dias e 5 horas à data e hora específicas
data_hora_futura = data_hora_especifica + timedelta(days=2, hours=5)

print(f"A data e hora específicas são: {data_hora_especifica}")
print(f"A data e hora após adicionar 2 dias e 5 horas: {data_hora_futura}")
```

## Explicação

Nesta solução, inicializamos o objeto `datetime` com uma data e hora específicas que são atribuídas à variável `data_hora_especifica`. Em seguida, utilizamos a classe `timedelta` para adicionar 2 dias e 5 horas à data e hora específicas. A operação de soma com o objeto `timedelta`, que é inicializado com os argumentos `days=2` e `hours=5`, retorna a data e hora futura que é atribuída à variável `data_hora_futura`. Finalmente, a data e a hora específicas e a data e a hora futura são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
