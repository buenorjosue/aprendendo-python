clone = { # Chave(key):Valor(value)
    "Nome":"Rex - CT-7567",
    "Origem":"Kamino",
    "Nascimento":"32 ABY",
    "Gênero":"Masculino"
}

# print(clone) # Imprime o dict inteiro
# print(clone["Origem"]) # Mostra o valor da chave

fab = clone.get("Origem") # fab = clone["Origem"]

clone["Origem"] = "Coruscant" # Mudando um dado

# for i in clone:
#    print(i,"|", clone[i]) # Chave e valor

for c,v in clone.items(): # Função que retorna a chave e o valor
    print(c, "|", v)

if "Nome" in clone:
    print("\nNome é uma chave")

print("Tamanho do Dictionary: ", len(clone)) # é dado pela quantidade de chaves

# clone["Batalhão"] = 501 # Adicionando uma chave

# clone.pop("Batalhão") # Removendo uma chave
# del clone["Batalhão"] # Tambem remove uma chave

clone.clear() # Remove tudo

nucleo = {
        "Coruscant":"Capital do Império",
        "Corellia":"Maior produção de Naves"
}

orlamedia = {
        "Naboo":"Planeta de Origem de Padmé",
        "Kashyyyk":"Lar dos Wookies"
}

regioes = {
    "R1":nucleo,
    "R2":orlamedia
}

print(regioes["R1"]["Coruscant"])
#print(planetas["Núcleo"]["Coruscant"])