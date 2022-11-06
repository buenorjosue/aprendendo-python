import os # Importando os comandos do sistema
os.system("cls") # Usando o comando de limpar o terminal 

"""
nome = input("Digite seu nome: ") # Função input que funciona como o gets ou scanf
print("Seu nome é",nome)
# input() 
"""

num1 = input("Digite o primeiro valor: ") # Tudo que é retornado em input é string
num2 = input("Digite o segundo valor: ")

res = int(num1) + int(num2)
print("A soma foi igual a: ", res)