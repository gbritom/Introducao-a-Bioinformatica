# Neste arquivo se aproveita as questões 3 e 4.

def manipulaSubstr(string):
    if string[0] != '>':
        substring_size = 3
        chave = ""
        conta, aux = 0, 0
        tam = len(string)
        substr = dict()
        for i in range(tam - substring_size + 1):
            s = string[i : i + substring_size]
            if s in substr:
                substr[s] += 1
            else:
                substr[s] = 1
        for key in substr.keys():
            aux += 1  # conta a posição
            # verificando qual é o maior valor
            if conta < substr[key]:
                conta = substr[key]
        var = str((max(substr, key=substr.get),conta))
        var = var.replace('(','')
        var = var.replace("'",'')
        var = var.replace(')','')
        var = var.replace(',','')

        return (var)
    else:
        return string

# Leitura de um Arquivo
filename = "sequence.fasta"
output = "results.txt"
lista = []
contador = 0
with open(output, "w") as op:
    # Lendo todo o arquivo, linha a linha
    with open(filename) as fp:
        seq = ""
        for linha in fp:
            linha = linha.rstrip()
            if seq != "":
                lista.append((header, seq))
                seq = ""
            header = linha[0:]
            op.write(manipulaSubstr(linha[:]+' '))
            contador+=1
            if contador%2 == 0:
                op.write('\n')
        else:
            seq += linha