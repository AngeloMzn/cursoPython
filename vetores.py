n = int(input("digite o tamanho do vetor ="))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero ="))

for i in range(0, n):
    print(vet[i])