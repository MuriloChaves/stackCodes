dicionario = {
    'dois': 2,
    'tres': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'baguncado': 1,
    'outro baguncado': 1
}

remover_itens = []

for chave, valor in dicionario.items():
    dicionario[chave] = dicionario[chave] -1
    if dicionario[chave] == 0:
        remover_itens.append(chave)

for item in remover_itens:
    dicionario.pop(item)

print(dicionario)