import os
import random

erros = 0
sorteado = random.randrange(0,100) # Gerando um número aleatorio

jogador = int(input("Digite um número: "))

while(sorteado != jogador):
    os.system("cls")
    if(sorteado > jogador):
        print("O número é maior, tente de novo")
    elif (sorteado < jogador):
        print("O número é menor, tente de novo")
    erros += 1
    jogador = int(input("Digite um novo número: "))
os.system("cls")
print("O número era: ", jogador, "- Você acertou em ", erros, "Tentativas")