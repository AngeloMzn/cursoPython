a = int(input("Digite um numero ="))
x = 0
print("Voce digitou =", a)
while a > 5:
    x += 1
    a -= 1

print("x =", x)
y = 0

for i in range(a):
    y += 1
print("y =", y)

for j in range(0, 5):
    print("j =", j)

for n in range(0, 5, 2): # terceiro parametro define de quanto em quanto incrementa ou decrementa(para decrementar usar numero negativo ex: -2)
    print("n =", n)
