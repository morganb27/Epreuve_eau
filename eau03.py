import sys
liste_Fibonacci = []

def suite_Fibonacci():

    i = 0
    a = 1
    b = 0
    while i < 1000:
        liste_Fibonacci.append(b)
        a, b = b, a + b
        i = i + 1

suite_Fibonacci()

try:
    if int(sys.argv[1]) >= 0:
        print(liste_Fibonacci[int(sys.argv[1])])

except IndexError:
    print("L'index se situe en dehors des limites de la liste.")

except:
    print("Erreur.")

