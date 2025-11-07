# Exercício 2.3 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se uma letra digitada pelo usuário é uma vogal ou consoante.

## Solução

```python
letra = input("Digite uma letra: ").lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
```

## Explicação

Neste código, solicitamos ao usuário que digite uma letra e armazenamos o valor na variável `letra`. Em seguida, convertemos a letra para minúscula usando o método `lower()`. Verificamos se a letra é uma vogal ou consoante usando a estrutura condicional `if`, comparando-a diretamente com cada uma das vogais usando o operador `or`. Se a letra for igual a qualquer uma das vogais ('a', 'e', 'i', 'o' ou 'u'), é uma vogal; caso contrário, é uma consoante. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
