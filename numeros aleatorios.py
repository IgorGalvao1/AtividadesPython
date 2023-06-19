import random
a = random.randint(0,10)
b = random.randint(0,10)

while True:
    print(f'Qual a multiplicação de {a} X {b}? ')
    result = float(input(''))
    mult = a * b
    if result == mult:
        print('Você acertou!!!')
        break
    else:
        print('Você ERROU!!!')
        continuar = (str(input('Você deseja continuar?    '))).lower()
        if continuar == ('sim'):
            continue
       


