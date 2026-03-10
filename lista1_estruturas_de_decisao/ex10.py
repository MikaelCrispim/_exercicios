horario = {
    'M':'Bom dia',
    'T':'Boa tarde',
    'N':'Boa noite'
}
periodo = input("Informe o horário que você estuda: (M)anhã, (T)arde ou (N)oite: ").upper()


if periodo in horario:
    print(horario[periodo])
else:
    print("Valor inválido")
