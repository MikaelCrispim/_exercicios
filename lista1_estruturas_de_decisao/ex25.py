p1 = input("Telefonou para vítima (S ou N)").upper()
p2 = input("Esteve no local do crime (S ou N)").upper()
p3 = input("Mora perto da vítima (S ou N)").upper()
p4 = input("Devia para a vítima (S ou N)").upper()
p5 = input("Já trabalhou com a vítima (S ou N)").upper()

respostas = [p1, p2, p3, p4, p5]

totalSim = respostas.count("S")

if totalSim == 2:
    classificacao = "Suspeito"
elif 3 <= totalSim <= 4:
    classificacao = "Cúmplice"
elif totalSim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(classificacao)