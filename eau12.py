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

def tri_a_bulle():
    for i in range(len(int_liste)-1):
        for j in range (0, len(int_liste)-i-1):
            if int_liste[j+1] < int_liste[j]:
                (int_liste[j], int_liste[j+1]) = (int_liste[j+1], int_liste[j])


tri_a_bulle()

for element in int_liste:
    print(element, end = " ")
