def media():
    n1 = input("Digite a primeira nota: ")
    n2 = input("Digite a segunda nota: ")
    m = (int(n1) + int(n2))/2
    print("Sua média é:", m)

media()

n3 = 10
n4 = 5

def calculos():
    op = input("Escolha a operação [+/-]: ")

    if (op == "+"):
        soma = n3 + n4
        print("Soma = ", soma)
    elif (op == "-"):
        subtrair = n3 - n4
        print("Subtração = ", subtrair)
    else:
        print("Operação invalida")
calculos()