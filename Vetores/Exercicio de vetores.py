L = []
print(L)
L = [0] * 5
print(L)
L = [0,0,0,0,0]
print(L)
L = [1,2,3,4,5]
print(L)
L = ['a','b']
print(L)
L = list()
print(L)
num = "456"
L = list(num)
print(L)


#O comando len mostra quantos elementos tem dentro da lista 
L = [1,2,3,4,5]
print (len(L))

#usando while
L = [1,2,3,4,5]
X = 0
while X < len(L):
    print(L[X],end= " ")
    X+=1

#usando for
B = [9,8,7,6,5]
for i in range(5):
    print(B[i],end=" ")