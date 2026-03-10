frase = input("Insira uma frase").upper()
vogais = {
    1:'A',
    2:'E',
    3:'I',
    4:'O',
    5:'U'
}
espacos = frase.count(" ")
vogal = 0
for i in frase:
    if i in vogais.values():
        vogal += 1
print(f"A frase possui {vogal} vogais e {espacos} espaços")