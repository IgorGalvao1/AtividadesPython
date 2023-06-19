from random import randint
L = []
M = []
for i in range(20):
    num = int(randint(1,50))
    L.append(num)#Vai adicionar o numero gerado na lista
    if num%5 ==0:#Verifica se o numero é multiplo de 5
        M.append(num)#Adiciona os numeros multiplos de 5 na lista
print(L)
print(f'Os numeros multiplos de 5 são {M}.')
