from random import randint
totalpares = 0
pares = []
total = 0

for i in range(20):
    num = int(randint(1,50))
    if num%2 == 0:
        total = total + num #Soma dos numeros pares
        totalpares = totalpares + 1 #Conta quantos numeros são pares
        pares.append(num) #Adiciona os numeros pares em uma lista
media = total / totalpares #Divide a soma pela quantidade
print(f'A soma de todos os numeros pares é {total}')
print(f'{totalpares} numeros são pares. Os numeros pares são {pares}. Sua media é {media:.2f}')