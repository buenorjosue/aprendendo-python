res = num = numero = 0

canal = "ManowJozui"

def cn():
    global abc # Declarando uma variavel local como global
    abc = "Olá, Mundo"
    print(canal)
cn()
print(abc)