filename = "sequence.fasta"
lista = []
# Lendo todo o arquivo, linha a linha
with open(filename) as fp:
    seq = ""
    for linha in fp:
        linha = linha.rstrip()
        if ">" == linha[0]:
            if seq != "":
                lista.append((header, seq))
                seq = ""
            header = linha[1:]
        else:
            seq += linha

for tupla in lista:
    print(tupla)

