from random import randint
M = []

for i in range(0,10):
    M.append([])
    count = 0
    for j in range(0,10):
        num = randint(5,38)
        M[i].append(num)
        count = count + num
    for b in range(10):
        print(count)
        
print(M)

#VERSÂO DO PROFESSOR

M = []
for i in range(10):
    soma = 0
    M.append([])
    for j in range(10):
        M[i].append(randint(5,38))
        soma = soma + M[i][j]
    print(f"A soma dos numeros digitados da linha {i+1} é: {soma}")
for cont in range(10):
    print(M[cont])