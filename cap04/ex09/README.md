# Exercício 4.9 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar um CPF e use uma expressão regular para verificar se o CPF está no formato DDD.DDD.DDD-DD, onde D corresponde a um dígito entre 0 e 9.

## Solução

```python
import re

cpf = input("Digite um CPF no formato 999.999.999-99: ")
padrao_cpf = r'd{3}\.\d{3}\.\d{3}-\d{2}'

if re.fullmatch(padrao_cpf, cpf):
    print("CPF no formato correto.")
else:
    print("CPF em formato incorreto.")
```

## Explicação

O programa inicia importando o módulo `re`, necessário para trabalhar com expressões regulares. Em seguida, solicita ao usuário para digitar um CPF, armazenando a entrada na variável `cpf`. A variável `padrao_cpf` contém a expressão regular `"`` d{3` . d{3} . d{3}- d{2}}`"`, que define o formato do CPF: três dígitos, um ponto, mais três dígitos, outro ponto, mais três dígitos, um hífen, e finalmente dois dígitos. A função `re.fullmatch` verifica se a *string* `cpf` corresponde exatamente ao padrão da expressão regular. Se corresponder, imprime que o CPF está no formato correto, caso contrário, informa que o formato está incorreto.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
