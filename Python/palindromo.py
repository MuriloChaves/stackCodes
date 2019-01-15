input_string = input('Entre com as palavras que deseja verificar se são um palíndromos: ').lower().split()

list_fragmented_word = []

for word in input_string:
    for char in word:
        list_fragmented_word.append(char)

if list_fragmented_word == list_fragmented_word[::-1]:
    print('SIM')
else:
    print('NÃO')
