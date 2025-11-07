# Exercício 1.26 - Fundamentos da Linguagem

## Enunciado

(**Difícil**) Crie um programa que peça ao usuário para digitar a altitude inicial de um objeto em queda livre a partir do repouso. Em seguida, o programa deve calcular e mostrar o tempo que o objeto leva para atingir o solo, desconsiderando a resistência do ar.

## Solução

```python
import math

g = 9.81 
h = float(input("Altitude inicial do objeto em metros: "))
t = math.sqrt((2*h)/g)
print(f"O objeto levará {t:.2f} segundos para atingir o solo.")
```

## Explicação

De acordo com a física, o tempo t em que um objeto em queda livre atinge o solo pode ser calculado pela equação t = sqrt((2*h)/g), onde h é a altura inicial e g é a aceleração devida à gravidade. Neste código, `import math` é um comando para importar a biblioteca "math" do Python, que contém funções matemáticas. No caso deste código, a função `sqrt` (raiz quadrada) é usada. A linha `g = 9.81`, define a constante g como 9.81, que é a aceleração da gravidade na Terra em metros por segundo ao quadrado. A linha seguinte, `h = float(...)`, pede ao usuário para inserir a altitude inicial do objeto em metros. O valor inserido é convertido para um número do tipo `float` (número real) e armazenado na variável `h`. Agora vem a parte principal, que é a aplicação da fórmula de queda livre da física, que é computada na linha `t = math.sqrt((2*h)/g)`. Por fim, o programa imprime o tempo com duas casas decimais..

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
