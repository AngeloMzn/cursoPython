m = int(input("digite o numero de linhas: "))
n = int(input("digite o numero de colunas"))

mat = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(0, m):
    for j in range(0, n):
        print(mat[i][j])
