#Metodo MATRIZ [INDICE1], [INDICE2]
M = [0] *2
for i in range(0,2):
    M[i]=[0] *3
    for j in range(0,3):
        M[i][j]=int(input("Digite o valor [{}][{}] -> ".format(i,j)))
print(M)

#Metodo APPEND

M =[]
for i in range(0,2):
    M.append([])
    for j in range (0,3):
        M[i].append(int(input("Digite valor [{}][{}] -> ".format(i,j))))
print(M)

# Versão sem .format
M =[]
for i in range(0,2):
    M.append([])
    for j in range (0,3):
        M[i].append(int(input(f"Digite o valor [{i}][{j}] ->")))
print(M)
