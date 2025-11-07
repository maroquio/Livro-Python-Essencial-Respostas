# Exercício 10.10 - Programação Concorrente

## Enunciado

Escreva um programa que crie uma `thread` para cada item de uma lista de 3 URLs de sites a seu gosto. Cada `thread` deve fazer uma solicitação HTTP para a sua URL e imprimir o conteúdo da resposta.

## Solução

```python
import threading
import requests

def get_url(url):
    response = requests.get(url)
    print(f"Conteúdo da URL {url}: {response.text}")

if __name__ == "__main__":
    urls = [
        'https://maroquio.com',        
        'https://youtube.com/maroquio',
        'https://python.org'
    ]

    for url in urls:
        threading.Thread(target=get_url, args=(url,)).start()
```

## Explicação

Nesta solução, criamos uma função chamada `get_url` que aceita uma URL, faz uma solicitação HTTP GET para a URL e imprime o conteúdo da resposta. No processo principal, criamos uma `thread` para cada URL em uma lista de URLs. Cada `thread` faz uma solicitação a uma URL e imprime o conteúdo da resposta.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
