from random import randint
M = []

for i in range(0,10):
    M.append([])
    for j in range(1,10):
        num = randint(0,50)
        M[i].append(num)
    
    print(f"O menor numero da lista {i+1} é {min(M[i])}")
for cont in range(10):
    print(f'Lista {cont+1}: {M[cont]}')

    #VERSÃO DO PROFESSOR

M = []
for i in range(10):
    menor = 50
    M.append([])
    for j in range(10):
        M[i].append(randint(1,50))
        if M[i][j] < menor:
            menor = M[i][j]
    print(f"O menor numero da linha {i+1} é: {menor}")
for cont in range(10):
    print(M[cont])