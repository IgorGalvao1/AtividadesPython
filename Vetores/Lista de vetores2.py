L = [0]*10
print(L)
for i in range(10):
    L[i] = int(input("{}º valor -> ".format(i+1)))
print(L)


#metodo APPEND

L=[]
print(L)
for i in range(10):
    valor = int (input("{}º valor -> ".format(i+1)))
    L.append(valor)
print(L)