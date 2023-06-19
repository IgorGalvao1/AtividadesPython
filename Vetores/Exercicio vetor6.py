from random import randint
X = int(input('Digite um valor para multiplicar:  '))
A = []
B = []
for i in range(10):
    num =int(randint(1,50))
    A.append(num)
for i in range(10):
   R = A[i] * X
   B.append(R)
print(A)
print(B)