x = 1 # Int
x = "Curso" # String
x = 15.6 # Float
x = False # Boolean

n1 = 1; n2 = 2; x = complex(n1,n2) # Número Complexo 'complex(1j)'

''' # Comentando um grupo de linhas
print(x.real) # Parte Real do n complexo
print(x.imag) # Parte Imaginária do n complexo
'''

x = ["Carro","Avião","Navio", 1, 58.3] # Array List
x[1] = "Ônibus" # Atribuindo um valor a uma posição

x = ("Carro","Elevador","Navio", 2, 34.3) # Tupla (ela é fechada e não aceita mudança)
# x[1] = "Bicicleta"

x = range(0,100,1) # Cria uma lista de 0 até 100

x = { # Dict
    "canal":"ManowJozui",
    "Idade":"20",
    "Nome":"Josué"
}

x = {1,23,19, 2, 3,2} # Tipo set: ordena e não repete valores

x = frozenset({12,34,2,1,2}) # Não pode ser modificado

print("Valor de x: " , x) # Imprindo o valor de x
print("Tipo de x: " , type(x)) # Imprindo o tipo de x