from random import randint
print('Digite qual opção você deseja: \n Opção 1: Ordem normal.\nOpção 2: Ordem inversa.')
L = []
L2 = []
op = int(input())
for i in range(10):
        num = int(randint(1,50))
        L.append(num)
        listarev = list(reversed(L))
if op == 1:
    print(L)
else:
    print(f'Ordem normal: {L}.')
    print(f'Ordem inversa: {listarev}')

    #ou 
#else:
    for i in range (9,-1,-1):
        L2.append(L[i])
    print(f'Ordem normal: {L}.')
    print(f'Ordem inversa: {L2}')
