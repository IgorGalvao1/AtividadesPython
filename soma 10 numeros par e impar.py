pares = 0
impares = 0
for i in range(10):
    num=int(input('insira um numero\n'))
    if num%2==0:
        pares = pares + num
    else:
        impares = impares + num
    print('Soma dos pare:  ',pares)
    print('Soma dos impares:  ',impares)