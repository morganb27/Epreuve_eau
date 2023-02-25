import sys

liste = []
int_liste = []
i = 1

try:
    while i < len(sys.argv):
        liste.append(sys.argv[i])
        i = i + 1

    for element in liste:
        element_int = int(element)
        int_liste.append(element_int)

except IndexError:
    pass

except:
    print("Erreur.")


def tri_par_selection():
    n = len(int_liste)
    for i in range (n):
        min = i
        for j in range(i+1, n):
            if int_liste[j] < int_liste[min]:
                min = j

        int_liste[i], int_liste[min] = int_liste[min], int_liste[i]

tri_par_selection()

print(int_liste)
