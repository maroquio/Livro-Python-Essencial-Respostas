# Exercício 4.25 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que adicione 30 dias à data atual utilizando `timedelta`.

## Solução

```python
from datetime import datetime, timedelta

# Obtém a data atual
data_atual = datetime.now()

# Adiciona 30 dias à data atual
data_futura = data_atual + timedelta(days=30)

print(f"A data atual é: {data_atual}")
print(f"A data após 30 dias será: {data_futura}")
```

## Explicação

Nesta solução, inicialmente importamos as classes `datetime` e `timedelta` do módulo `datetime`. A função `datetime.now()` é utilizada para obter a data e a hora atuais que são atribuídas à variável `data_atual`. A classe `timedelta` é usada para representar uma duração, a diferença entre duas datas ou tempos. Adicionamos 30 dias à data atual utilizando a operação de soma com o objeto `timedelta` que é inicializado com o argumento `days=30`. A data resultante é atribuída à variável `data_futura`. Finalmente, as duas datas são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
