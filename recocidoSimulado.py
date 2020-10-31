import random
import math

def sigmoid(gamma):
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    return 1 / (1 + math.exp(-gamma))

def calcularValor(aux):
    valor = 0
    for x in range(5):
        if(x == 0 and aux[x] == 1):
            valor = valor + 28
        if(x == 1 and aux[x] == 1):
            valor = valor + 22
        if(x == 2 and aux[x] == 1):
            valor = valor + 18
        if(x == 3 and aux[x] == 1):
            valor = valor + 6
        if(x == 4 and aux[x] == 1):
            valor = valor + 1
    return valor

def calcularPeso(aux):
    valor = 0
    for x in range(5):
        if(x == 0 and aux[x] == 1):
            valor = valor + 7
        if(x == 1 and aux[x] == 1):
            valor = valor + 6
        if(x == 2 and aux[x] == 1):
            valor = valor + 5
        if(x == 3 and aux[x] == 1):
            valor = valor + 2
        if(x == 4 and aux[x] == 1):
            valor = valor + 1
    return valor

temp = 100
cambio = 0.1
solucion = []
s = []
for y in range(5):
    s.append(random.randint(0, 1))
for x in range(20):
    print()
    sx = []
    for y in range(5):
        sx.append(random.randint(0, 1))

    print(calcularValor(sx), ">=", calcularValor(s), end =" ")
    if(calcularValor(sx) >= calcularValor(s) and 12 > calcularPeso(sx)):
        s = sx.copy()
        print("- Si")
    else:
        print("- No")
        print(sigmoid((calcularValor(s) - calcularValor(sx))/temp), ">", random.uniform(0, 1), end =" ")
        if(sigmoid((calcularValor(s) - calcularValor(sx))/temp) > random.uniform(0, 1) and 12 > calcularPeso(sx)):
            print("- Si")
            s = sx.copy()
        else:
            print("- No")
    temp = temp*cambio
    print(temp)
    print(s)
print(s)
