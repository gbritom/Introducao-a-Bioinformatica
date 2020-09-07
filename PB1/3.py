#Aproveitando tudo da vídeo aula.

string = input("Digite a sequência: ")
substring_size = 4
quantidade = 0
tam = len(string)
substr = dict()
for i in range(tam - substring_size + 1):
    s = string[i : i + substring_size]
    if s in substr:
        substr[s] += 1
    else:
        substr[s] = 1
for key in substr.keys():
    quantidade += 1

print(quantidade)
