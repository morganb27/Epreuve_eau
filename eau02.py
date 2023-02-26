import sys

#Définition de la fonction

def parametres_envers():
    i = 1
    while i < (len(sys.argv)):
        print(sys.argv[len(sys.argv)-i])
        i = i + 1


#Appel de la fonction

parametres_envers()


