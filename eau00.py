import numpy as np

tableau_3d = np.zeros((8, 3, 10), dtype=int)

for i in range(8):
    for j in range(2):
        for k in range(10):
            if k != i and k != j:
                if i < 6:
                    tableau_3d[i, j, k] = k
                elif i == 6 and k < 8:
                    tableau_3d[i, j, k] = k
                elif i == 7 and k == 7:
                    break
                else:
                    tableau_3d[i, j, k] = k

print(tableau_3d)
