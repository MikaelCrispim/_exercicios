print("1 - Filé Duplo\n2 - Alcatra\n3 - Picanha")
tipoCarne = int(input("Escolha o tipo de carne: "))
quantidadeKg = float(input("Quantidade (Kg): "))
cartaoTabajara = input("Pagamento no Cartão Tabajara? (S/N): ").upper()

if tipoCarne == 1:
    nomeCarne = "Filé Duplo"
    precoUnitario = 4.90 if quantidadeKg <= 5 else 5.80
elif tipoCarne == 2:
    nomeCarne = "Alcatra"
    precoUnitario = 5.90 if quantidadeKg <= 5 else 6.80
else:
    nomeCarne = "Picanha"
    precoUnitario = 6.90 if quantidadeKg <= 5 else 7.80

precoTotal = quantidadeKg * precoUnitario
valorDesconto = precoTotal * 0.05 if cartaoTabajara == "S" else 0
valorPagar = precoTotal - valorDesconto

print(f"Tipo: {nomeCarne}")
print(f"Quantidade: {quantidadeKg} Kg")
print(f"Preço Total: R$ {precoTotal:.2f}")
print(f"Desconto: R$ {valorDesconto:.2f}")
print(f"Valor a Pagar: R$ {valorPagar:.2f}")
