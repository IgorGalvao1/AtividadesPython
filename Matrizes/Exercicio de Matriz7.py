from random import randint
M = []
contador = 0
total = 0
for i in range (0,10):
    M.append([])
    for j in range (0,10):
        num = (randint(1,50))
        M[i].append(num)
        total = total + num
        contador = contador + 1
print(M)
print(f"A media é de {total / contador}")

#VERSÂO DO PROFESSOR

from random import randint
M = []
contador = 0
total = 0
for i in range (0,10):
    M.append([])
    for j in range (0,10):
        M[i].append(randint(1,50))
        total = total + M[i][j]
for cont in range(10):
    print(M[cont])
print(f"A media é de {total / 100}")