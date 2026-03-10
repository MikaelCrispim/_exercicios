notas = []

for i in range(2):
    i = float(input("Insir sua nota: "))
    notas.append(i)

media = sum(notas) / len(notas)

print("Sua Média foi: " + media)
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
else:
    print("Reprovado")