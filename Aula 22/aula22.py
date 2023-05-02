soma = lambda a,b:a+b

#print(soma(2,5))

mult = lambda a,b,c:(a+b)/c

#print(mult(1,2,3))

#print((lambda a,b:a*b)(12,10))

r = lambda x,func:x+func(x)

print(r(2, lambda x:x*x))

r = lambda x,func:x+func(x)

print(r(3, lambda x:x+4))