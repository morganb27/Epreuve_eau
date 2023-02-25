import sys

liste = []

i = 1

try:
    while i < 20:
        liste.append(sys.argv[i])
        i = i + 1

except IndexError:
    pass

except:
    print("Erreur.")

if len(liste) == len(set(liste)):
    print("-1")
else:
    print(liste.index(liste[-1]))

