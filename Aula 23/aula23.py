import random

class Mago:
    vida = 0
    magia_preparada = False
    magia = ""

m1 = Mago()
m2 = Mago()
m3 = Mago()

m1.vida = (8 + random.randrange(1,9))
m1.magia = "Fireball"
m1.magia_preparada = True

pronto = "Sim" if m1.magia_preparada else "Não"

print("Quantidade de vida do mago:", m1.vida)
print("Magia que ele tem:", m1.magia)
print("Magia preparada?", pronto)