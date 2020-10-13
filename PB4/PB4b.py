import numpy as np
import math
D_pssm = [['Pos', '1', '2', '3', '4', 'Overall Freq'],
          ['A', 0, 0, 0, 0, 0],
          ['T', 0, 0, 0, 0, 0],
          ['G', 0, 0, 0, 0, 0],
          ['C', 0, 0, 0, 0, 0]]
conteudo = []
with open("D.motif.scores", "w")as op:
    with open("D.motif") as fp:
        for linha in fp:
            linha = linha.replace('\t', ' ')
            linha = linha.replace('\n', '')
            conteudo.append(linha)
        fp.close()

    for y in range(4):
        A, T, G, C = 0, 0, 0, 0  # occorências / count
        for char in conteudo:
            if char[y] == 'A':
                A = A + int(char[5:])
            elif char[y] == 'T':
                T = T + int(char[5:])
            elif char[y] == 'G':
                G = G + int(char[5:])
            elif char[y] == 'C':
                C = C + int(char[5:])
        # arrendonda até a 4ª casa decimal
        D_pssm[1][y+1] = round(A/(A+T+G+C), 4)
        D_pssm[1][5] = D_pssm[1][5] + D_pssm[1][y+1]
        D_pssm[2][y+1] = round(T/(T+A+G+C), 4)
        D_pssm[2][5] = D_pssm[2][5] + D_pssm[2][y+1]
        D_pssm[3][y+1] = round(G/(G+T+A+C), 4)
        D_pssm[3][5] = D_pssm[3][5] + D_pssm[3][y+1]
        D_pssm[4][y+1] = round(C/(C+T+G+A), 4)
        D_pssm[4][5] = D_pssm[4][5] + D_pssm[4][y+1]

    D_pssm[1][5] = round(D_pssm[1][5]/4, 4)
    D_pssm[2][5] = round(D_pssm[2][5]/4, 4)
    D_pssm[3][5] = round(D_pssm[3][5]/4, 4)
    D_pssm[4][5] = round(D_pssm[4][5]/4, 4)

    for y in range(4):
        if y >= 1:
            D_pssm[1][y] = round(D_pssm[1][y]/D_pssm[1][5], 4)
            D_pssm[2][y] = round(D_pssm[2][y]/D_pssm[2][5], 4)
            D_pssm[3][y] = round(D_pssm[3][y]/D_pssm[3][5], 4)
            D_pssm[4][y] = round(D_pssm[4][y]/D_pssm[4][5], 4)

    for y in range(4):
        if y >= 1:
            D_pssm[1][y] = round(np.log2(D_pssm[1][y]), 4)
            D_pssm[2][y] = round(np.log2(D_pssm[2][y]), 4)
            D_pssm[3][y] = round(np.log2(D_pssm[3][y]), 4)
            D_pssm[4][y] = round(np.log2(D_pssm[4][y]), 4)

    D_array = np.array(D_pssm)
    for x in range(5):
        linha = str(D_pssm[x])
        linha = linha.replace('[', '')
        linha = linha.replace(' ', '')
        linha = linha.replace(']', '')
        linha = linha.replace(',', '\t')
        linha = linha.replace("'", '')
        op.write(linha+'\n')
    op.close()
