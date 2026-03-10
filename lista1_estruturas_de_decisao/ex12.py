valorHora = float(input("Informe quanto você recebe por hora: "))
qtdTrabalhada = float(input("Informe quantas horas você trabalha: "))

ir1500 = 0.05
ir2500 = 0.1
ir2501 = 0.2

salarioBruto = valorHora * qtdTrabalhada

FGTS = salarioBruto * 0.11
INSS = salarioBruto * 0.1
SINDICATO = salarioBruto * 0.03

if salarioBruto > 900:
    totalDesconto = (salarioBruto * ir1500) + INSS + SINDICATO
    print(f'''
        O salário bruto é R$ {salarioBruto}
        IR R$ {salarioBruto * ir1500}
        INSS R$ {INSS}
        FGTS R$ {FGTS}
        Sindicato R$ {SINDICATO}
        Total de descontos R$ {totalDesconto}
        Salário Liquido R$ {salarioBruto - totalDesconto}
''')
elif salarioBruto > 1500:
    totalDesconto = (salarioBruto * ir2500) + INSS + SINDICATO
    print(f'''
        O salário bruto é R$ {salarioBruto}
        IR R$ {salarioBruto * ir2500}
        INSS R$ {INSS}
        FGTS R$ {FGTS}
        Sindicato R$ {SINDICATO}
        Total de descontos R$ {totalDesconto}
        Salário Liquido R$ {salarioBruto - totalDesconto}
''')
elif salarioBruto > 2500:
    totalDesconto = (salarioBruto * ir2501) + INSS + SINDICATO
    print(f'''
        O salário bruto é R$ {salarioBruto}
        IR R$ {salarioBruto * ir2501}
        INSS R$ {INSS}
        FGTS R$ {FGTS}
        Sindicato R$ {SINDICATO}
        Total de descontos R$ {totalDesconto}
        Salário Liquido R$ {salarioBruto - totalDesconto}
''')
else:
    totalDesconto = INSS + SINDICATO
    print(f'''
        O salário bruto é R$ {salarioBruto}
        INSS R$ {INSS}
        FGTS R$ {FGTS}
        Sindicato R$ {SINDICATO}
        Total de descontos R$ {totalDesconto}
        Salário Liquido R$ {salarioBruto - totalDesconto}
''')