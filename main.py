import math
figury = int(float(input().strip()))
lista = []
figura = []
wynik = 0
for element in range(figury):
    lista.append(input().split())

def pole_kola(x):
        return math.pi * x * x
def pole_prostokata(x,y):
        return x * y
def pole_trojkata(x,y,z):
        return (wzor*(wzor-x)*(wzor-y)*(wzor-z)) ** 0.5
for figura in lista:
    if len(figura) == 1:
        x = float(figura[0])
        wynik += pole_kola(x)
    elif len(figura) == 2:
        x = float(figura[0])
        y = float(figura[1])
        wynik += pole_prostokata(x,y)
    elif len(figura) == 3:
        x = float(figura[0])
        y = float(figura[1])
        z = float(figura[2])
        wzor = ((x + y + z)/2)
        wynik+= pole_trojkata(x,y,z)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        break
print(round(wynik,2))