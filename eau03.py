import sys
liste_Fibonacci = []

#Définition de la fonction

def suite_Fibonacci():

    i = 0
    a = 1
    b = 0
    while i < 1000:
        liste_Fibonacci.append(b)
        a, b = b, a + b
        i = i + 1

suite_Fibonacci()

#Résolution et gestion des erreurs

try:
    if int(sys.argv[1]) >= 0:
        print(liste_Fibonacci[int(sys.argv[1])]) #On appelle le N-ième élément de liste_Fibonacci

except IndexError:
    print("L'index se situe en dehors des limites de la liste.")

except:
    print("Erreur.")

