# Exercício 10.2 - Programação Concorrente

## Enunciado

Modifique o programa anterior para que ele utilize quatro processos em vez de dois e compare os tempos de execução. A lista de números deve ser dividida igualmente entre os quatro processos.

## Solução

```python
import multiprocessing

def soma_numeros(numeros, retorno):
    retorno.put(sum(numeros))

if __name__ == "__main__":
    numeros = list(range(1, 99999999))
    quarto = len(numeros) // 4
    retorno1 = multiprocessing.Queue()
    retorno2 = multiprocessing.Queue()
    retorno3 = multiprocessing.Queue()
    retorno4 = multiprocessing.Queue()
    processo1 = multiprocessing.Process(target=soma_numeros, args=(numeros[:quarto], retorno1))
    processo2 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto:quarto*2], retorno2))
    processo3 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto*2:quarto*3], retorno3))
    processo4 = multiprocessing.Process(target=soma_numeros, args=(numeros[quarto*3:], retorno4))
    processo1.start()
    processo2.start()
    processo3.start()
    processo4.start()
    processo1.join()
    processo2.join()
    processo3.join()
    processo4.join()
    resultado_final = retorno1.get() + retorno2.get() + retorno3.get() + retorno4.get()
    print(f"A soma total é {resultado_final}")
```

## Explicação

Nesta solução, modificamos a solução do exercício anterior para usar quatro processos em vez de dois. Dividimos a lista de números em quatro partes iguais e cada processo ficou responsável por somar uma parte. Cada processo coloca seu resultado em uma `Queue`, que é então recuperada pelo processo principal para calcular a soma total. Apesar da quantidade de processos ter dobrado, observe que o tempo de execução não caiu pela metade. Isso ocorre porque a criação de contexto de um processo pelo sistema operacional também tem um custo computacional considerável. Neste caso, temos o gargalo é do tipo *CPU Bound*, porém, não é complexo o suficiente para que o uso uso de *multiprocessing* traga grandes vantagens.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
