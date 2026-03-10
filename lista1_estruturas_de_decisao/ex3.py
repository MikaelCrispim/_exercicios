sexo = input("Informe seu sexo (M) Masculino ou (F) Feminino:")
sexos = {'Masculino':'M', 'Feminino':'F'}

if sexo.upper() in sexos.values():
    if sexo == 'M':
        print("Sexo Masculino")
    else:
        print("Sexo Feminino")
else:
    print("Sexo inválido")