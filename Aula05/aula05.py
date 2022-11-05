import random # Importando a Biblioteca do Random

num_i = 10
num_f = 10.3
num_c = 10j

# num_r = random.randrange(0,59) # Pegando um número aleatório entre 0 e 59

num_r = [ # Criando uma lista com 6 números aleatórios
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100)
]

x = num_r

# x = int(num_f) # Convertendo float para inteiro
# x = float(num_i) # Convertendo int para float

print("Valor: ", x[0])
print("Valor: ", x[1])
print("Valor: ", x[2])
print("Valor: ", x[3])
print("Valor: ", x[4])
print("Valor: ", x[5])