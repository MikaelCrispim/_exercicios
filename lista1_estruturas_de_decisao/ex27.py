kgMorango = float(input("Kg de morangos: "))
kgMaca = float(input("Kg de maçãs: "))

if kgMorango <= 5:
    precoMorango = kgMorango * 2.50
else:
    precoMorango = kgMorango * 2.20

if kgMaca <= 5:
    precoMaca = kgMaca * 1.80
else:
    precoMaca = kgMaca * 1.50

pesoTotal = kgMorango + kgMaca
valorBruto = precoMorango + precoMaca

if pesoTotal > 8 or valorBruto > 25:
    valorFinal = valorBruto * 0.90
else:
    valorFinal = valorBruto

print(f"Valor a ser pago: R$ {valorFinal:.2f}")
