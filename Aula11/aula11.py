'''
a = 10
b = 5 
op = "+"
res = 0 

if op == "+": # Operação de comparação == 
    res = a + b
elif op == "-": # Else if em python
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
else:
    print("Operador Invalido!")

print(a, op, b, "=", int(res))
'''

clima = "Sol"
dinheiro = 1000
lugar = ""

if clima == "Sol" or (dinheiro >= 300 and dinheiro <= 500): # Operação de "&& = and" e de "|| = or"
    lugar = "Clube"
else:
    lugar = "Cinema"

print("Vou ao", lugar)