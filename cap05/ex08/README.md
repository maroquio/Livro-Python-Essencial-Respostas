# Exercício 5.8 - Funções

## Enunciado

Você é um investigador e precisa decifrar uma mensagem secreta escondida em um texto. Cada letra da mensagem foi substituída pela letra do alfabeto que vem imediatamente depois dela. Por exemplo, "a" foi substituída por "b", "b" foi substituída por "c", e assim por diante. A letra "z" foi substituída por "a". Escreva uma função recursiva chamada decifrar_mensagem que aceite a mensagem codificada como uma *string* e retorne a mensagem decodificada. A regra é que a função deve ser recursiva!

## Solução

```python
def decifrar_mensagem(mensagem):
    if len(mensagem) == 0:
        return mensagem
    else:
        char_decifrado = chr((ord(mensagem[0]) - 98) % 26 + 97)
        return char_decifrado + decifrar_mensagem(mensagem[1:])

print(decifrar_mensagem('bdfn'))  
# Saída: 'acem'
```

## Explicação

Nesta solução, o objetivo principal é decifrar a mensagem letra por letra. A lógica aqui é aplicar uma função recursiva que chama a si mesma até que o comprimento da mensagem seja zero. A condição base da função recursiva é que a função retorna a mensagem (que neste ponto é uma *string* vazia) se o comprimento da mensagem for zero. Isso serve para terminar a recursão. Caso contrário, a função calcula a letra original para o primeiro caractere da mensagem (ou seja, `mensagem[0]`) usando o comando {chr((ord(mensagem[0]) - 98) \

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
