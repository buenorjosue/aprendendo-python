curso = " Curso de Python "

print(curso.strip()) # Função para tirar o espaço do inicio e do fim

print(curso.lower()) # Converte os Maiusculo para minusculos
print(curso.upper()) # Converte os Minusculos para maiusculos

print(curso.replace("Python","Java")) # Substitui a parte desejada por outra

a = curso.split(" ") # Transforma cada parte em um elemento do array
print(a)

print(curso[0:6]) # Imprindo apenas um intervalo especifico na String

print("Tamanho:" , len(curso)) # Função para ver o tamanho da String
