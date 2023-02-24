import sys

nombre_premier = []


def nbre_premier():
    i = 1
    a = 1
    while i <= 200:
        if a > 1:  # on vérifie si a est supérieur à 1
            b = True
            for j in range(2, a-1):
                if a % j == 0:
                    b = False
                    break  # on sort de la boucle for si a n'est pas premier
            if b == True:
                nombre_premier.append(a)
                i = i + 1  # on incrémente i si a est premier
        a += 1

nbre_premier()

k = int(sys.argv[1])

for element in nombre_premier:
    if element > k:
        print(element)
        break



