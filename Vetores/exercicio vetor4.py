from random import randint
L = []
M = []
numero = int(input('Digite um numero para verificar se existem numeros multiplos:  '))
for i in range(20):
    num = int(randint(1,50))
    L.append(num)
    if num%numero == 0:
        M.append(num)

print(L)
print(f'Os numeros multiplos de {numero} são {M}.')
