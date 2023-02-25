import sys

liste = []
i = 1
int_liste = []

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

int_liste.sort()
print(int_liste)

def minimum_absolue(int_liste):
    difference_minimum = int_liste[1] - int_liste[0]
    for j in range(1, len(int_liste)-1):
        difference = int_liste[j+1] - int_liste[j]
        if difference < difference_minimum:
            difference_minimum = difference
    return difference_minimum

minimum_absolue(int_liste)

print(minimum_absolue(int_liste))


