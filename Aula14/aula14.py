import os

"""
os.system("cls")

clones = ["Rex","Cody","Fives","Heavy","Echo"]
i = 0 # controle
tam = len(clones)
while i < tam: # Estrutura do While e a condição
    print("Clone[",i,"] =", clones[i])
    i+=1  # aumentando o controle
print("\nFim do Loop")
"""

rebels = []
rebel = input("Digite um membro da rebelião: ")

while rebel != "-1":
    rebels.append(rebel)
    print("Digite '-1' para sair")
    rebel = input("Digite um membro da rebelião: ")

os.system("cls")

for i in rebels:
    print(i)