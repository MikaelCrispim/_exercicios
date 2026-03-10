telefone = input("Informe o numero de telefone com 7 ou 8 digitos: ")

telefonePuro = telefone.replace("-", "").replace(" ", "")

if len(telefonePuro) == 7:
    telefoneCorrecao = '3' + telefonePuro
    print(f"O telefone corrigido é: {telefoneCorrecao}")
elif len(telefonePuro) == 8:
        print(f"O telefone é: {telefonePuro}")
else:
    print("Telefone incorreto!")
