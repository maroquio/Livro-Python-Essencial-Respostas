# Capítulo 10 - Exercício 6
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
