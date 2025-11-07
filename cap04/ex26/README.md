# Exercício 4.26 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que subtraia 2 horas da hora atual utilizando `timedelta`.

## Solução

```python
from datetime import datetime, timedelta

# Obtém a hora atual
hora_atual = datetime.now()

# Subtrai 2 horas da hora atual
hora_anterior = hora_atual - timedelta(hours=2)

print(f"A hora atual é: {hora_atual}")
print(f"A hora 2 horas atrás era: {hora_anterior}")
```

## Explicação

Nesta solução, utilizamos a função `datetime.now()` para obter a data e a hora atuais que são atribuídas à variável `hora_atual`. A classe `timedelta` é usada para subtrair 2 horas da hora atual utilizando a operação de subtração com o objeto `timedelta` que é inicializado com o argumento `hours=2`. A hora resultante é atribuída à variável `hora_anterior`. Finalmente, as duas horas são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
