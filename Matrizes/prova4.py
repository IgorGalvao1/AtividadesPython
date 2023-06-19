from random import randint
M = []
impar = 0
for i in range(0,5):
    M.append([])
    for j in range(0,5):
        num = randint(10,99)
        M[i].append(num)
        if (M[i][j]) %2 != 0:
            impar = impar + 1
    print(f'Lista {i+1} tem {impar} impares')
    impar = 0
       
for i in range (5):
    if num %2 !=0:
        impar = impar + 1
    print(f"Lista {1+i}: {M[i]}")
