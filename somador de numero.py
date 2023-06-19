numero = int(input('Digite um numero: '))
soma = 0
while True:
    while numero != 0:
        soma += numero
        numero = int(input('Digite um numero: '))
    if numero == 0:
        print(f'Sua soma total é igual a {soma}')
        
        break

