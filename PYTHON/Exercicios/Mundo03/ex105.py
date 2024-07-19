def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de cada aluno.
    :param sit: valor opcional(True ou False), exibe a situação da turma (BOA, RAZOÁVEL ou RUIM).
    :return: dicionário com base nos dados fornecidos.
    """
    
    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)

    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    
    return turma

A1 = notas(5.5, 2.5, 1.5, sit=True)

print(A1)
help(notas)