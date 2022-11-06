clones = ["Rex", "Cody", "Fives", "Echo"]
clones.append("Boba Fett") # Função que insere elementos na lista
clones.append("Hunter")
clones.append("Omega")

# clones[3] = "Boba Fett" # Inserindo numa posição especifica

# print(clones[-2]) # Imprindo da Direita para a esquerda

# Removendo Elementos:  #

# clones.remove("Boba Fett") # Removendo um elemento da lista

# clones.pop() # Removendo o ultimo elemento da lista

# del clones[2] # Removendo numa posição especifica

# clones.clear() # Remove todos os elementos da lista

# Trabalhando com 2 listas #

# clones2 = list(clones) # Copia tudo de uma lista para a outra

clones2 = ["Tech", "Wrecker", "Crosshair"]

clones3 = clones+clones2 # Juntando 2 listas

print(len(clones3),"clones na lista") # Imprimindo o tamanho da lista
print(sorted(clones3)) # Imprime em ordem alfabetica