import re


entrada = "toxinsNCBI.fna"
saida = "toxins_3-5.fna"
header = re.compile(">lcl\|(\w+.1_cds_)(\w+.1)")
seqRe = re.compile("^.*[A-T]$\n")


def traduz(seq):
    tmp = ""
    indice = 0
    while indice < len(seq):
        if (seq[indice] == 'A'):
            tmp += 'T'
        elif (seq[indice] == 'C'):
            tmp += 'G'
        elif (seq[indice] == 'T'):
            tmp += 'A'
        elif (seq[indice] == 'G'):
            tmp += 'C'
        indice += 1
    return tmp


with open(saida, "w") as op:
    with open(entrada) as fp:
        seq = ""
        for linha in fp:
            if header.match(linha):
                if seq:  # se existe algo (!= "")
                    op.write(traduz(seq[::-1])+'\n')
                    seq = ""  # reseta a seq ao encontra novo header
                match = header.match(linha)
                match.groups()
                op.write(match.group(2)+'\n')

            elif seqRe.match(linha):
                linha = linha.rstrip()  # remove quebra de linha
                seq += linha  # grava seq
        op.write(traduz(seq[::-1])+'\n')  # grava última seq.
