import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    while a < b :
        print (a, end = " ")
        a = a + 1

    while b < a:
        print(b, end = " ")
        b = b + 1

except:
    print("Erreur")