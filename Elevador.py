a = int(input("Digite a capacidade maxima em KG: "))
b = int(input("Digite o peso da primeira pessoa em KG: "))
c = int(input("Digite o peso da segunda pessoa em KG: "))
d = int(input("Digite o peso da terceira pessoa em KG: "))
e = int(input("Digite o peso da quarta pessoa em KG: "))
f = int(input("Digite o peso da quinta pessoa em KG: "))
g = b+c+d+e+f
if a>g:
    print("Excedeu a carga maxima")
else:
    print("Acesso liberado")
