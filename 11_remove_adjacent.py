"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    # """ Resposta 1 """
    # response = [nums[0]] if nums else []
    # for index in range(1, len(nums)):
    #     if nums[index - 1] != nums[index]:
    #         response.append(nums[index])
    
    # return response

    # """ Resposta 2 """
    # adjacent = nums[1:] + [None]
    # return [num for i, num in enumerate(nums) if num != adjacent[i]]

    # """ Resposta 3 """
    # adjacents = nums[1:] + [None]
    # tuples = zip(nums, adjacents)
    # return [tuple_[0] for tuple_ in tuples if tuple_[0] != tuple_[1]]

    """ Resposta 4 """
    return [tuple_[0] for tuple_ in zip(nums, nums[1:] + [None]) if tuple_[0] != tuple_[1]]


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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
