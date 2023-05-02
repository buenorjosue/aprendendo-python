import random

class Guerreiro:
    vida = 0
    acordado = True
    nome = ""
    def __init__(self, v, a, n):
        self.vida = v
        self.acordado = a # self é igual o this em outras linguagens
        self.nome = n
    def mostrar(self):
        print("Quantidade de vida do Guerreiro:", self.vida)
        print("Seu nome é:", self.nome)
        sleep = "Sim" if self.acordado else "Não"
        print("Ele está acordado?", sleep)
        print("----------------------------------")
    def dormir(self):
        self.acordado = False
    def acordar(self):
        self.acordado = True
    def atacar(self):
        if(self.acordado):
            print("Atacando!")
        else:
            print("Está dormindo!")

g1 = Guerreiro((10 + random.randrange(1,11)), False, "Trant'or Kan")
g2 = Guerreiro((10 + random.randrange(1,11)), True, "Balthram, o Honrado")

g2.mostrar()
g2.atacar()