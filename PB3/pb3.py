import numpy as np
import re
seqRe = re.compile("(\w+)[A-T]$")

pt = {'match': 1, 'mismatch': -1, 'gap': -2}


def mch(a, b):
    if a == b:
        return pt['match']
    elif a == '-' or b == '-':
        return pt['gap']
    else:
        return pt['mismatch']


def NWAlign(s1, s2):  # NWA = Needleman–Wunsch alignment
    m, n = len(s1), len(s2)
    pontuacao = np.zeros((m+1, n+1))  # preenche com zeros

    # Inicialização
    for i in range(m+1):
        pontuacao[i][0] = pt['gap'] * i
    for j in range(n+1):
        pontuacao[0][j] = pt['gap'] * j

    # Preenchimento
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diagonal = pontuacao[i-1][j-1] + mch(s1[i-1], s2[j-1])
            remove = pontuacao[i-1][j] + pt['gap']
            insere = pontuacao[i][j-1] + pt['gap']
            pontuacao[i][j] = max(diagonal, remove, insere)

    print('Matriz de Pontuação: \n%s\n' % pontuacao)
    alinhamento1, alinhamento2 = '', ''
    i, j = m, n

    # Caminho de volta
    while i > 0 and j > 0:
        pontuacao_atual = pontuacao[i][j]
        pontuacao_diagonal = pontuacao[i-1][j-1]
        pontuacao_esq = pontuacao[i][j-1]
        pontuacao_cima = pontuacao[i-1][j]

        if pontuacao_atual == pontuacao_diagonal + mch(s1[i-1], s2[j-1]):
            a1, a2 = s1[i-1], s2[j-1]
            i, j = i-1, j-1
        elif pontuacao_atual == pontuacao_cima + pt['gap']:
            a1, a2 = s1[i-1], '-'
            i -= 1
        elif pontuacao_atual == pontuacao_esq + pt['gap']:
            a1, a2 = '-', s2[j-1]
            j -= 1
        alinhamento1 += a1
        alinhamento2 += a2

    while i > 0:
        a1, a2 = s1[i-1], '-'
        alinhamento1 += a1
        alinhamento2 += a2
        i -= 1

    while j > 0:
        a1, a2 = '-', s2[j-1]
        alinhamento1 += a1
        alinhamento2 += a2
        j -= 1

    alinhamento1 = alinhamento1[::-1]  # inverte
    alinhamento2 = alinhamento2[::-1]  # inverte
    seqN = len(alinhamento1)
    similaridade = ''
    seq_pontuacao = 0
    for i in range(seqN):
        a1 = alinhamento1[i]
        a2 = alinhamento2[i]
        if a1 == a2:
            similaridade += a1
            seq_pontuacao += mch(a1, a2)

        else:
            seq_pontuacao += mch(a1, a2)
            similaridade += ' '

    print("Pontuação = %d\n" % seq_pontuacao)
    print(alinhamento1)
    print(similaridade)
    print(alinhamento2)


entrada = "sequencias.fasta"
with open(entrada) as fp:
    seq1 = ""
    seq2 = ""
    for linha in fp:
        if seqRe.match(linha):  # se encontrar seq
            if seq1:  # se seq1 já existe, grava seq2
                seq2 = linha.rstrip()
            else:  # se não, grava seq1
                seq1 = linha.rstrip()
    NWAlign(seq1, seq2)
