import re

entrada = "mRNA_toxins.fna"
saida = "toxins.faa"
header = re.compile("(\w+.1)")
seqRe = re.compile("^.*[A-T]$\n")


def traduz(seq):
    saida = ""
    '''
    aproveitei a lógica da tradução do site: http://pythonfiddle.com/rna-to-protein/
    pois condizia com meu código, evitando escrever o segmento cordao mão-a-mão. 
    Depois de ter entendido a questão 1, que por acaso passei 3 dias quebrando a 
    cabeça, após isso as demais questões foram fluindo.
    '''
    triplets = [seq[i:i+3] for i in range(0, len(seq), 3)]
    cordao = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
              "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
              "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
              "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
              "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
              "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
              "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
              "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
              "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
              "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
    for triplet in triplets:
        if cordao.get(triplet, "X") == "Stop":
            saida += (cordao.get(triplet, "X"))
        else:
            saida += (cordao.get(triplet, "X"))
            continue
    return saida


with open(saida, "w") as op:
    with open(entrada) as fp:
        seq = ""
        for linha in fp:
            if header.match(linha):
                if seq:  # se existe algo (!= "")
                    op.write(traduz(seq)+'\n')
                    seq = ""  # reseta a seq ao encontra novo header
                match = header.match(linha)
                match.groups()
                op.write(match.group(0)+'\n')

            elif seqRe.match(linha):
                linha = linha.rstrip()  # remove quebra de linha
                seq += linha  # grava seq
        op.write(traduz(seq))  # grava última seq.
