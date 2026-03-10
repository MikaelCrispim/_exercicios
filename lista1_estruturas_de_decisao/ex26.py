opcao = input("A-álcool (1,90/L) ou G-gasolina (2,50/L)").upper()
qtdLitros = float(input("Quantos litros deseja abastecer "))

if opcao == "G":
    litroGaso = 2.50
    descGaso = 0.04 if qtdLitros <= 20 else 0.06
    brutoGaso = qtdLitros * litroGaso
    precoTotal = brutoGaso - (brutoGaso * descGaso)

elif opcao == "A":
    litroAlc = 1.90
    descAlc = 0.03 if qtdLitros <= 20 else 0.05
    brutoAlc = qtdLitros * litroAlc
    precoTotal = brutoAlc - (brutoAlc * descAlc)

else:
    print("Opção inválida")
print(f'''
    Valor Total: R$ {precoTotal}
    ''')