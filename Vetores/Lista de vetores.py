L = [9,8,7,6,5]
for i in range(5):
    print(L[i],end=" ")

#comando diferente que faz a mesma função

L = [1,2,3,2,1]
for item in L:
    print(item,end=" ")

L = [0]*10
print(L)
for i in range(10):
    L[i] = int(input("{} valor -> ".format(i+1)))