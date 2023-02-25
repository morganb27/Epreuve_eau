for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if (i < k) or (i == k and j < l):
                    print(str(i) + str(j) + " " + str(k) + str(l), end = ",")


