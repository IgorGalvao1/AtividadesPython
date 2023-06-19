num = int(input('Informe um numero -> '))
if num>999 and num<100:
    print('Numero invalido!!')
else:
    texto = str(num)
    print(texto)
    a = int(texto[0])
    b = int(texto[1])
    c = int(texto[2])
    if a<b and b<c:
        print('Crescente')
    elif a>b and b>c:
        print('Decrescente')
    else:
        print('Fora de ordem!')
