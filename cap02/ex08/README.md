# Exercício 2.8 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um texto digitado pelo usuário corresponde a uma data no formato "dd/mm/aaaa", considerando que a data deve ter 10 caracteres, "dd" deve variar de 01 a 31, "mm" de 01 a 12 e "aaaa" de 0001 a 9999. Utilize colchetes para acessar os caracteres do texto pelo seu índice (exemplos: texto[0:2] pega os dois primeiros dígitos e texto[3:5] pega os dígitos nas posições 3 e 4).

## Solução

```python
texto = input("Digite uma data (dd/mm/aaaa): ")

if len(texto) == 10 and texto[2] == '/' and texto[5] == '/':
    dia = int(texto[:2])
    mes = int(texto[3:5])
    ano = int(texto[6:])

    if (1 <= dia <= 31) and (1 <= mes <= 12) and (1 <= ano <= 9999):
        print("Data válida no formato 'dd/mm/aaaa'.")
    else:
        print("Data inválida no formato 'dd/mm/aaaa'.")
else:
    print("O texto não corresponde a uma data.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um texto e armazenamos o valor na variável `texto`. Verificamos se o texto tem o formato "dd/mm/aaaa" usando a estrutura condicional `if`. Primeiro, verificamos se o comprimento do texto é igual a 10 e se os caracteres nas posições 2 e 5 são barras (/). Se as condições forem atendidas, extraímos o dia, o mês e o ano do texto usando fatiamento de *strings* e os convertemos para inteiros. Em seguida, verificamos se os valores extraídos estão dentro de um intervalo válido para dia, mês e ano. Se todas as condições forem atendidas, o texto corresponde a uma data no formato "dd/mm/aaaa"; caso contrário, não corresponde. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
