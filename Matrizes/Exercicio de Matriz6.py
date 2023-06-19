M =[]
contador = 0
for i in range(0,2):
    M.append([])
    for j in range (0,3):
        num = (int(input(f"Digite o valor [{i}][{j}] ->")))
        M[i].append(num)
        contador = contador  + num
print(M)
print(f"A soma de todos os numeros das matrizes são {contador}")