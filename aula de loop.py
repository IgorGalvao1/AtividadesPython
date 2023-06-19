#Tabuada do numero ate 10
number = int(input('DIGITE UM NÚMERO PARA SABER A TABUADA:'))
multi = 0
result = 0
while multi <= 10:
  result = number * multi
  print(f'{number} x {multi} = {result}')
  multi = multi + 1
  

else:
  print('Acabou, não tem mais jeito')