menor = int(input("entre com o menor numero da faixa de busca: "))
maior = int(input("Entre com o maior numero da faixa de busca: "))

print("Os numeros primos entre {0} e {1} são: ",format(menor,maior))
for num in range(menor,maior + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) = 0:
                break
            else:
                print(num)