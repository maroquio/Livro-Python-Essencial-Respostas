# Exercício 4.10 - Números, Textos, Datas e Horas

## Enunciado

Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, use expressão regular para extrair todos os artigos da frase. Ao fim, o programa deve mostrar a frase sem os artigos.

## Solução

```python
import re

frase = input("Digite uma frase: ")
frase_sem_artigos = re.sub(r"ba\b|\bo\b|\bas\b|\bos\b|\bum\b|\buns\b|\buma\b|\bumas\b", "", frase, flags=re.IGNORECASE)
print(frase_sem_artigos)
```

## Explicação

Nesta solução, a biblioteca `re` é usada para manipular expressões regulares. O usuário insere uma frase e a função `re.sub()` é usada para substituir todas as ocorrências de artigos ("a", "o", "as", "os", "um", "uns", "uma", "umas") na frase por nada (ou seja, remove-os). O resultado é impresso. Note-se que o `flags=re.IGNORECASE` garante que a substituição é feita independentemente do termo estar em maiúscula ou minúscula. A letra `r` antes da *string* indica que ela está em formato *raw*, ou seja, as barras invertidas serão consideradas de forma literal, e não como caracteres de escape.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
