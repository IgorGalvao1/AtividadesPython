from random import randint
M = []
soma = 0
somainv = 0
for i in range(0,5):
    M.append([])
    for j in range(0,5):
        num = randint(1,50)
        M[i].append(num)
for k in range(5):
    print(M[k])

diagonal = []
diagonalinv = []
for i in range(len(M)):
    for j in range(len(M[0])):
        if i == j:
            diagonal.append(M[i][j])
            soma = soma + (M[i][j])
for j in range(len(M)):
    for i in range(len(M[0])):
        if i == j:
            diagonal.append(M[i][j])
            somainv = somainv + (M[i][j])
print()
print(f'A diagonal principal é {diagonal}')
print(f'A soma da diagonal principal é {soma}')