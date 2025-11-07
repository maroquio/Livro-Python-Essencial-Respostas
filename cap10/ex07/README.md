# Exercício 10.7 - Programação Concorrente

## Enunciado

Modifique o programa anterior para usar um `threading.Lock` a fim de evitar condições de corrida.

## Solução

```python
import threading
import urllib.request

def download_file(url, filename, lock):
    with lock:
        urllib.request.urlretrieve(url, filename)

if __name__ == "__main__":
    urls = [
        'https://picsum.photos/2000?random=1',
        'https://picsum.photos/2000?random=2',
        'https://picsum.photos/2000?random=3'
    ]

    lock = threading.Lock()
    
    for i, url in enumerate(urls):
        threading.Thread(target=download_file, args=(url, f'file{i}.jpg', lock)).start()
```

## Explicação

Nesta solução, modificamos a solução do exercício anterior para usar um `threading.Lock` para evitar condições de corrida. O `Lock` é adquirido antes de chamar a função `urlretrieve` e liberado após a função retornar. Isso garante que apenas uma `thread` baixe um arquivo por vez.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
