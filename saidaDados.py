print("bom dia ", end ='') # end = '' retira a quebra de linha
print("boa noite")

# placeholder de formatação
# int   -> %d
# float -> %f
# str   -> %s


x = "maria"
y = 19

print("%s tem %d anos" %(x, y))


a: float

x = 2.2456

print("{:.2f}".format(x))

nome = "Maria Silva"
sexo = 'F'
salario = 5000.45
idade = 27
print("A funcionaria {:s}, sexo {:s}, ganha {:f} e tem {:d} anos".format(nome, sexo, salario, idade))