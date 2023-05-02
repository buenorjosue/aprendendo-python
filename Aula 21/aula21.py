valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def somar(num):
    r = 0 
    for n in num:
        r += n 
    return r

def imprimir(val):
    print("Os valores da lista são:")
    for v in val:
        print(v)

#imprimir(valores)
print(valores ,"\n","Soma =", somar(valores))