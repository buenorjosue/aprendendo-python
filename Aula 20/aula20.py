def soma(*num):
    r = 0 
    for n in num:
        r += n 
    print("Resultado = ", r)

#soma()

# Utilizando argumentos arbitrários

def texto(*t):
    print(t[7], t[8], t[12])

#texto("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

# Utilizando argumentos padrões

def clones(c="Hunter"):
    print("Nome do clone: " + c)
#clones()    

# Passando uma lista como parametro

valores = [1,2,3,4,5]
def somar(num):
    r = 0 
    for n in num:
        r += n 
    print("Resultado = ", r)

somar(valores)