def fatorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return int(a * fatorial(a - 1))


valor = int(input("Digite o valor para receber seu fatorial: "))
print("%i! = %i" %(valor, fatorial(valor)))