# Exercício 7.20 - Arquivos, Módulos e Pacotes

## Enunciado

Com o ambiente virtual ativado, use o comando `deactivate` para desativar o ambiente virtual "pratica_venv" e, em seguida, tente importar a biblioteca `requests` novamente. O que acontece?

## Solução

```python
# No terminal
deactivate
```

## Explicação

Neste exercício, o comando `deactivate` é usado para desativar o ambiente virtual "pratica_venv". Depois de desativar o ambiente virtual e tentar importar a biblioteca `requests` no interpretador Python, você provavelmente receberá um erro de importação, a menos que a biblioteca `requests` também esteja instalada no ambiente Python global. Isso ocorre porque desativar o ambiente virtual retorna você ao Python global, que não tem acesso às bibliotecas instaladas no ambiente virtual "pratica_venv".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
