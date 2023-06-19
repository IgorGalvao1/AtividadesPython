M = [[1,2,3],[4,5,6]]
for i in range (0,2):
    for j in range(0,3):
        print("[{:^3}] ".format(M[i][j]),end = ' ') #:^3 Serve para o conteudo ficar no meio de 3 espaços
    print()
