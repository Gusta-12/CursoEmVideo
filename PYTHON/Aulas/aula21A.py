# Docstring (Documento/Manual de um comando)
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da conttagem
        :param p: passo da contagem
        :return: sem retorno
    """ # SEMPRE deve estar logo abaixo do comando DEF
        # 'param' = parâmetro
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


help(contador)