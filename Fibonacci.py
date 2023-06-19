num = int(input('Digite quantos numeros deseja na sequência de Fibonacci:    '))
numanterior = 0
fibo = 1
if num == 1:
    print(numanterior)
elif num == 2:
    print(numanterior)
    print(fibo)
else:
    print(numanterior)
    for i in range (num-1):
        print(fibo)
        numanterior,fibo = fibo,fibo + numanterior


