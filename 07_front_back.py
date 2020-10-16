"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

import math

def front_back(a, b):
    """ Resposta 1 """
    # half_a = math.ceil(len(a) / 2)
    # half_b = math.ceil(len(b) / 2)
    # return a[:half_a] + b[:half_b] + a[half_a:] + b[half_b:]

    """ Resposta 2 """
    # half_a, half_b = map(math.ceil, (len(a) / 2, len(b) / 2))
    # return "".join([a[:half_a], b[:half_b], a[half_a:], b[half_b:]])

    """ Resposta 3 """
    # def half(string, last_part=False):
    #     middle = math.ceil(len(string) / 2)
    #     return string[middle:] if last_part else string[:middle]

    # last_half = lambda s : half(s, last_part=True)
    # return "".join([half(a), half(b), last_half(a), last_half(b)])

    """ Resposta 4 """
    def split(string):
        middle = math.ceil(len(string) / 2)
        return (string[:middle], string[middle:])
    
    def mix(tuple1, tuple2):
        return tuple1[0], tuple2[0], tuple1[1], tuple2[1]

    return "".join(mix(split(a), split(b)))



# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
