char = input("Insira uma única letra: ")
vogais = {
    1:'A',2:'E',3:'I',4:'O',5:'U'
}
if char.upper() in vogais.values():
    print("A letra é uma vogal")
else:
    print("A letra é uma consoante")