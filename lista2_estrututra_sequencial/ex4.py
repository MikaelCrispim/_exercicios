notas = []
for i in range(1, 5):
    i = float(input(f"Insira sua nota do {i}° Bimestre: "))
    notas.append(i)

media = sum(notas) / len(notas)
print(f"Sua média é {media:.1f}")
