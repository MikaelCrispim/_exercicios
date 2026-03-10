cpf = input("Informe o CPF (formato xxx.xxx.xxx-xx): ")
cpf = cpf.replace('.', '').replace('-', '')

if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF Inválido")
else:
    soma1 = 0
    peso1 = 10
    for i in range(9):
        soma1 = soma1 + (int(cpf[i]) * peso1)
        peso1 = peso1 - 1
        
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1

    soma2 = 0
    peso2 = 11
    for i in range(10):
        soma2 = soma2 + (int(cpf[i]) * peso2)
        peso2 = peso2 - 1
        
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    if str(digito1) == cpf[9] and str(digito2) == cpf[10]:
        print("CPF Válido")
    else:
        print("CPF Inválido")