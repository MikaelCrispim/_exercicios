salario = float(input("Informe seu salário: "))

if salario <= 280:
    novoSalario = salario * 1.2
    print(
        f'''
        O salário antes do reajuste era {salario}
        O percentual de aumento foi de 20%
        O valor do aumento foi {salario * 0.2}
        O salário atual é {novoSalario}"
          ''')
elif salario > 280 and salario <= 700:
    novoSalario = salario * 1.15
    print(
        f'''
        O salário antes do reajuste era {salario}
        O percentual de aumento foi de 15%
        O valor do aumento foi {salario * 0.15}
        O salário atual é {novoSalario}"
          ''')
elif salario > 700 and salario <= 1500:
    novoSalario = salario * 1.1
    print(
        f'''
        O salário antes do reajuste era {salario}
        O percentual de aumento foi de 10%
        O valor do aumento foi {salario * 0.1}
        O salário atual é {novoSalario}"
          ''')
else:
    novoSalario = salario * 1.05
    print(
        f'''
        O salário antes do reajuste era {salario}
        O percentual de aumento foi de 5%
        O valor do aumento foi {salario * 0.05}
        O salário atual é {novoSalario}"
          ''')