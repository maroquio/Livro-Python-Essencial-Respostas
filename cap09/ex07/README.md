# Exercício 9.7 - Tratamento de Exceções

## Enunciado

Crie uma classe `Triangulo` com os atributos `lado1`, `lado2` e `lado3`. Implemente um método `tipo_triangulo` que informe se o triângulo é equilátero, isósceles ou escaleno. Utilize tratamento de exceções para lidar com triângulos inválidos.

## Solução

```python
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise ValueError("Todos os lados devem ser maiores que zero.")
            if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
                raise ValueError("A soma de quaisquer dois lados deve ser maior que o terceiro lado.")
            if self.lado1 == self.lado2 == self.lado3:
                return "Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Isósceles"
            else:
                return "Escaleno"
        except ValueError as e:
            print(e)

triangulo = Triangulo(3, 4, 5)
print(triangulo.tipo_triangulo())
```

## Explicação

A classe `Triangulo` possui três atributos para representar os lados de um triângulo. O método `tipo_triangulo` primeiro verifica se todos os lados são maiores que zero. Se não forem, uma `ValueError` é lançada com uma mensagem apropriada. Em seguida, verifica-se se a soma de quaisquer dois lados é maior que o terceiro lado, que é uma regra para todos os triângulos. Se essa regra for violada, outra `ValueError` é lançada. Finalmente, se essas duas verificações passarem, determinamos se o triângulo é equilátero (todos os lados são iguais), isósceles (dois lados são iguais) ou escaleno (todos os lados são diferentes) e retornamos a classificação correspondente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
