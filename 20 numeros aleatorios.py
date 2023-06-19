import random
lista = []
for a in range(20):
    var = random.randint(0,10)
    print(var)
    lista.append(var)
    lista.sort()
print(f'O maior numero é {lista[-1]}')


#ou

import random
maior = 0
for i in range(20):
    num = random.randint(0,10)
    if num >= maior:
        maior = num
    print(num, end='  ')
print()
print(f'O maior número encontrado foi {maior}')
