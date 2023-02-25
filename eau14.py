import sys

liste = []
liste_ascii = []


i = 1
j = 0

try:
    while i < len(sys.argv):
        liste.append(sys.argv[i])
        i = i + 1


except IndexError:
    pass

except:
    print("Erreur.")


def ordre_ascii():
    for i in range(len(liste)):
        for j in range(i, len(liste)):
            if ord(liste[i][0]) > ord(liste[j][0]):
                liste[i], liste[j] = liste[j], liste[i]
    return liste

ordre_ascii()

liste_ascii = ordre_ascii()

i = 0
while i < len(liste_ascii):
    print(liste_ascii[i], end = " ")
    i = i + 1