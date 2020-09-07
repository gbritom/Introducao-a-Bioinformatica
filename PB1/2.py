def calculaGC(sequencia):
    a, t, g, c = 0, 0, 0, 0
    for letra in sequencia:
        if letra == "g":
            g += 1
        elif letra == "c":
            c += 1
        elif letra == "t":
            t += 1
        elif letra == "a":
            a += 1
    valor = 100 * (g + c) / (g + c + a + t)
    return f"{valor}%"


a = input("Informe a sequência: ")
print(calculaGC(a))
