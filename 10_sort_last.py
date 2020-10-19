"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.
"""
def sort_last(tuples):
    # """ Resposta 1"""
    # def sort(tuple):
    #     return tuple[-1]
    # return sorted(tuples, key=sort)

    # """ Resposta 2"""
    # return sorted(tuples, key=lambda tuple : tuple[-1])

    # """ Resposta 3"""
    # from operator import itemgetter
    # return sorted(tuples, key=itemgetter(-1))

    """ Resposta 4"""
    def last_item_sort(tuple):
        return tuple[-1]
    return rover_sorted(tuples, key=last_item_sort)

def rover_sorted(tuples, key=lambda item : item):
    if not tuples:
        return []
    
    items_values = list(map(key, tuples))
    min_index = items_values.index(min(items_values))
    min_item = tuples.pop(min_index)
    return [min_item] + rover_sorted(tuples, key)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sort_last, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 6), (2, 2), (1, 5)],
         [(2, 2), (1, 3), (1, 5), (3, 4, 6), (1, 7)])