#Tabuada do numero ate 10
number = int(input('DIGITE UM NÚMERO PARA SABER A TABUADA:'))
multi = 0
result = 0
while multi <= 10:
  result = number * multi
  print(f'{number} x {multi} = {result}')
  multi = multi + 1
  
if multi >= 11:
    outro = str(input('Deseja ver a tabuada de outro numero?: ')).lower()
    while outro == 'sim':
        number = int(input('DIGITE UM NÚMERO PARA SABER A TABUADA:'))
        multi = 0
        result = 0
        while multi <= 10:
         result = number * multi
         print(f'{number} x {multi} = {result}')
         multi = multi + 1
         if multi >= 11:
             outro = str(input('Deseja ver a tabuada de outro numero?: ')).lower()
    if outro == 'não':
        print('Fim')
    