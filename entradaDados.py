nome = input("digite o nome = ") # le string
idade = int(input("digite a idade = ")) # ler int
salario = float(input("digite o salario = ")) # ler um float

print("{:s} de idade {:d} recebe {:.2f}".format(nome, idade, salario))