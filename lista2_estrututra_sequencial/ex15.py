valorHora = float(input("Informe quanto você recebe por hora: "))
qtdTrabalhada = float(input("Informe quantas horas você trabalha: "))

salarioBruto = valorHora * qtdTrabalhada

IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
SINDICATO = salarioBruto * 0.05

totalDesconto = IR + INSS + SINDICATO
print(f'''
        O salário bruto é R$ {salarioBruto}
        Total de descontos R$ {totalDesconto}
        Salário Liquido R$ {salarioBruto - totalDesconto}
    ''')