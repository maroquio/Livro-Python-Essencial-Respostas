# Exercício 10.6 - Programação Concorrente

## Enunciado

Escreva um programa Python que utilize `multithreading` para baixar 3 arquivos da internet simultaneamente. Você pode usar imagens aleatórias de 2000 pixels de altura e largura geradas por https://picsum.photos/2000?random=1 (random=2, random=3, ...).

## Solução

```python
import threading
import urllib.request

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

if __name__ == "__main__":
    urls = [
        'https://picsum.photos/2000?random=1',
        'https://picsum.photos/2000?random=2',
        'https://picsum.photos/2000?random=3'
    ]

    for i, url in enumerate(urls):
        threading.Thread(target=download_file, args=(url, f'file{i}.jpg')).start()
```

## Explicação

Nesta solução, criamos uma função chamada `download_file`, que aceita uma URL e um nome de arquivo, e usa a função `urlretrieve` do módulo `urllib.request` para baixar o arquivo. No processo principal, criamos uma `thread` para cada URL que desejamos baixar, passando a URL e o nome do arquivo para a função `download_file`. Cada `thread` baixa um arquivo simultaneamente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
