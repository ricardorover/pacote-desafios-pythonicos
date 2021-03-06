"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict

def file_words(filename):
    with open(filename, 'r') as file:
        return file.read().lower().split()

def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de palavras subsequentes."""
    words = file_words(filename)
    usage_dict = defaultdict(set)

    for word, next_word in zip([""] + words, words + [""]):
        usage_dict[word].add(next_word)
    return usage_dict

def mimic(mimic_dict, word, limit=200):
    next_word = random.choice(tuple(mimic_dict[word]))
    return [word, " "] + mimic(mimic_dict, next_word, limit=limit-1) if limit > 0 else []

def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    print(''.join(mimic(mimic_dict, '')))

# Chama mimic_dict() e mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict_ = mimic_dict(sys.argv[1])
  print_mimic(dict_, '')


if __name__ == '__main__':
  main()
