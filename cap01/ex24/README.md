# Exercício 1.24 - Fundamentos da Linguagem

## Enunciado

Crie um programa que calcule e mostre a área de um triângulo retângulo dadas as medidas dos seus catetos como entrada.

## Solução

```python
cateto1 = float(input("Digite a medida do primeiro cateto (m): "))
cateto2 = float(input("Digite a medida do segundo cateto (m): "))

area = (cateto1 * cateto2) / 2

print(f"Área do triângulo retângulo: {area:.2f} m²")
```

## Explicação

Neste código, solicitamos ao usuário as medidas dos catetos do triângulo retângulo e armazenamos os valores nas variáveis `cateto1` e `cateto2`. Em seguida, calculamos a área do triângulo utilizando a fórmula `area = (cateto1 * cateto2) / 2`. Por fim, imprimimos o resultado formatado com duas casas decimais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
