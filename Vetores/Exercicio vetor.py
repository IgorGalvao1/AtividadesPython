from random import randint
totalpares = 0 
totalimpares = 0
for i in range(10):
    num = int(randint(1,50))
    print(num, end=" ")
    if num%2 == 0:
        totalpares = totalpares + 1
    else:
        totalimpares = totalimpares + 1
print()
print(f'Total pares: {totalpares}')
print(f'Total impares: {totalimpares}')