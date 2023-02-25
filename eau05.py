import sys

try:
        if sys.argv[2] in sys.argv[1]:
            print("True")
        else:
            print("False")
except:
    print("Erreur.")
