"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""

def fix_start(s):
    """ Resposta 1 """
    # return s[0] + s[1:].replace(s[0], "*")

    """ Resposta 2 """
    # return "".join([s[0]] + ["*" if s[index] == s[0] else s[index] for index in range(1, len(s))])

    """ Resposta 3 """
    # first = s[0]
    # return "".join([first] + ["*" if letter == first else letter for letter in s[1:]])

    """ Resposta 4 """
    return "".join(["*" if index != 0 and letter == s[0] else letter for index, letter in enumerate(s)])



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
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
