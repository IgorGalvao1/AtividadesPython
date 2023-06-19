a = int(input("digite o que você deseja calcular - caixa de papelão = 1, lata de óleo = 2: "))
if a == 1:
    b = float(input("digite a altura: "))
    c = float(input("digite a largura: "))
    d = float(input("digite o comprimento: "))
    r = b*c*d
    print(f"O volume da caixa da papelão é igual a {r} cm³")
else:
        e = float(input("Digite o raio: "))
        f = float(input("Digite o comprimento: "))
        g = 3.14159 * (e**2) *f
        print(f"O volume da lata de oleo é {g} cm³")