# curso = "Curso de Python"
# canal = "- Aula 07"

# res = curso+" "+canal # Concatenando Strings em Python

# palavra = "de"

# res = "Python" in curso # Verifica se a palavra "Python" está na variavel curso e retorna True ou False
# res = "Python" not in curso # Verifica se a palavra "Python" não está na variavel curso 

# res = palavra in curso # Verifica se a variavel está em na outra variavel 

cidade = "Rio de Janeiro"
dia = 5
mes = "Novembro"
ano = 2022
bd = "Bom dia!"

data = "{}, {} de {} de {} \n\"{}\"" # Metodo format  
# \n pula linha ; \" coloca em aspas ; \' coloca aspas simples ; \t tabulação ; \b apaga um caractere

print(data.format(cidade, dia, mes, ano, bd))