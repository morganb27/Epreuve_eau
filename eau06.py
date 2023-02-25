import sys

i = 0
l = 0
m = 1

a = sys.argv[1]
b = 7

try:

    if a.isdigit():
        print("Erreur.")
    else:
        while i < len(a):
            j = a[l]
            j = j.upper()
            print(j, end = "")
            k = a[m]
            k = k.lower()
            print(k, end = "")
            i = i + 1
            l = l + 2
            m = m + 2


except IndexError:
    print("")

except:
    print("Erreur.")