# Exercício 1.23 - Fundamentos da Linguagem

## Enunciado

Crie um programa que calcule e mostre o volume de uma esfera dado o seu raio como entrada.

## Solução

```python
raio = float(input("Digite o raio da esfera (m): "))

volume = (4/3) * math.pi * raio**3

print(f"Volume da esfera: {volume:.2f} m³")
```

## Explicação

Neste código, importamos a biblioteca `math` para utilizar a constante `math.pi`. Em seguida, solicitamos ao usuário o raio da esfera e calculamos o volume utilizando a fórmula `volume = (4/3) * math.pi * raio**3`. Por fim, imprimimos o resultado formatado com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
