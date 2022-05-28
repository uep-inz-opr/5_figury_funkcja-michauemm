import math
figury = int(float(input().strip()))
lista = []
figura = []
wynik = 0
for element in range(figury):
    lista.append(input().split())

def pole_kola(x):
        return pi * x * x
def pole_prostokata(x,y):
        return x * y
def pole_trojkata(x,y,z):
        return (s*(s-x)*(s-y)*(s-z)) ** 0.5
for figura in lista:
    if len(figura) == 1:
        a = float(figura[0])
        wynik += pole_kola(x)
    elif len(figura) == 2:
        a = float(figura[0])
        b = float(figura[1])
        wynik += pole_prostokata(x,y)
    elif len(figura) == 3:
        a = float(figura[0])
        b = float(figura[1])
        c = float(figura[2])
        s = ((a + b + c)/2)
        wynik+= pole_trojkata(x,y,z)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        break
print(round(pole,2))