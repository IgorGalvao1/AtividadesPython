from random import randint
A = []
for i in range(10):
    A.insert(i,randint(1,50))
print(f'Lista Gerada: {A}')

for i in range(10):
    for j in range(i+1,10):
        if A[i] > A[j]:
            A[i],A[j] = A[j],A[i]
print(f'Lista em Ordem: {A}')

