import sys

argument = sys.argv[1]
liste_argument = argument.split(" ")

try:
    if argument.isdigit():
        print("Erreur.")

    else:
        for mot in liste_argument:
            a = mot[0].upper()
            print(a, end = "")
            print(mot[1:], end = " ")

        print()

except:
    print("Erreur.")
