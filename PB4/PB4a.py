import numpy as np
import math
np.seterr(divide='ignore') #remove avisos de divisão por zero
C_pssm = [['Pos', '1', '2', '3', '4', '5', '6', '7', 'Overall Freq'],
          ['A', 0, 0, 0, 0, 0, 0, 0, 0],
          ['T', 0, 0, 0, 0, 0, 0, 0, 0],
          ['G', 0, 0, 0, 0, 0, 0, 0, 0],
          ['C', 0, 0, 0, 0, 0, 0, 0, 0]]
conteudo = []
with open("C.motif.scores", "w")as op:
    with open("C.motif") as fp:
        for linha in fp:
            linha = linha.replace('\t', ' ')
            linha = linha.replace('\n', '')
            conteudo.append(linha)
        fp.close()

    for y in range(7):
        A, T, G, C = 0, 0, 0, 0  # occorências / count
        for char in conteudo:
            if char[y] == 'A':
                A = A + int(char[8:])
            elif char[y] == 'T':
                T = T + int(char[8:])
            elif char[y] == 'G':
                G = G + int(char[8:])
            elif char[y] == 'C':
                C = C + int(char[8:])
        # arrendonda até a 4ª casa decimal
        C_pssm[1][y+1] = round(A/(A+T+G+C), 4)
        C_pssm[1][8] = C_pssm[1][8] + C_pssm[1][y+1]
        C_pssm[2][y+1] = round(T/(T+A+G+C), 4)
        C_pssm[2][8] = C_pssm[2][8] + C_pssm[2][y+1]
        C_pssm[3][y+1] = round(G/(G+T+A+C), 4)
        C_pssm[3][8] = C_pssm[3][8] + C_pssm[3][y+1]
        C_pssm[4][y+1] = round(C/(C+T+G+A), 4)
        C_pssm[4][8] = C_pssm[4][8] + C_pssm[4][y+1]

    C_pssm[1][8] = round(C_pssm[1][8]/7, 4)
    C_pssm[2][8] = round(C_pssm[2][8]/7, 4)
    C_pssm[3][8] = round(C_pssm[3][8]/7, 4)
    C_pssm[4][8] = round(C_pssm[4][8]/7, 4)
    C_array = np.array(C_pssm)
    print(C_array), print('\n')
    for y in range(7):
        if y >= 1:
            C_pssm[1][y] = round(C_pssm[1][y]/C_pssm[1][8], 4)
            C_pssm[2][y] = round(C_pssm[2][y]/C_pssm[2][8], 4)
            C_pssm[3][y] = round(C_pssm[3][y]/C_pssm[3][8], 4)
            C_pssm[4][y] = round(C_pssm[4][y]/C_pssm[4][8], 4)
    C_array = np.array(C_pssm)
    print(C_array), print('\n')
    for y in range(7):
        if y >= 1:
            C_pssm[1][y] = round(np.log2(C_pssm[1][y]), 4)
            C_pssm[2][y] = round(np.log2(C_pssm[2][y]), 4)
            C_pssm[3][y] = round(np.log2(C_pssm[3][y]), 4)
            C_pssm[4][y] = round(np.log2(C_pssm[4][y]), 4)
    C_array = np.array(C_pssm)
    print(C_array), print('\n')
    for x in range(5):
        linha = str(C_pssm[x])
        linha = linha.replace('[', '')
        linha = linha.replace(' ', '')
        linha = linha.replace(']', '')
        linha = linha.replace(',', '\t')
        linha = linha.replace("'", '')
        op.write(linha + '\n')
    op.close()
