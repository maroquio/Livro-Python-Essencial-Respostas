# Capítulo 10 - Exercício 10
# Livro: Python Essencial: Para Programadores
# Autor: Ricardo Maroquio

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
