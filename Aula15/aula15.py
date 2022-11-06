t_clones = ("Rex", "Cody","Echo") # Criando uma tupla - Servem para guardar dados Imutaveis

# Como alterar um elemento de uma tupla
l_clones = list(t_clones)
l_clones[1] = "Hunter"
t_clones = tuple(l_clones)

# t_clones[1] = "Traidor" # A Tupla não aceita adição nem modificação de itens depois de criada
# print(t_clones[2])

for i in t_clones:
    print(i)