kgPeixe = float(input("Informe quantos KG de peixe você coletou: "))
if kgPeixe > 50:
    multa = 4 * (kgPeixe - 50)
    print(f"Você excedeu em {kgPeixe - 50}Kg e vai pagar R${multa} de multa")
else:
    print("Você não excedeu o limite!")