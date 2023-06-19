from random import randint
M = []
for i in range (0,2):
    M.append([])
    for j in range(0,3):
        M[i].append(randint(1,50))
print(M)