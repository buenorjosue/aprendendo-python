"""
clones = ["Rex","Cody","Fives","Echo"] # Array/ List

clones[2] = "Hunter"

for i in clones:
    print(i)
"""

starwars = [ # Uma matriz (Arrays dentro de Array)
    ["Clone Force 99", "Hunter"],
    ["Regular", "Rex"],
    ["Sith","Darth Vader"],
    ["Ano", 2022]
]

starwars.append(["Criador","George Lucas"])

starwars[3][1] = 1977 # Alterando um valor na matriz

for l,c in starwars: # For em Matriz
    print(l," | ",c)

# print(starwars[0][1])