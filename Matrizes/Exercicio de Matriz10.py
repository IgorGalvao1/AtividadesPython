from random import randint
M = []
menor=50

for i in range(0,10):
    M.append([])
    for j in range(0,10):
        M[i].append(randint(1,50))
        if M[i][j]<menor:
            menor=M[i][j]
    print(f'O menor numero da coluna {j+1} é : {menor} ')
for cont in range(10):
  print(M[cont])

#Versão do girico

  from random import randint
M = []
menor=50

for i in range(0,10):
    M.append([])
    for j in range(0,10):
        M[i].append(randint(1,50))

for j in range(0,10):
  for i in range(0,10):
    if M[i][j]<menor:
      menor=M[i][j]
  print(f'menor numero da coluna {j+1} é : {menor} ')
  menor=50
for cont in range(10):
  print(M[cont])