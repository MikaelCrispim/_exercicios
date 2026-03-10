data = input("Informe uma data no formato dd/mm/aaaa: ")

date = data.split('/')

dia, mes, ano = int(date[0]), int(date[1]), int(date[2])

diasMes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if bissexto:
    diasMes[2] = 29

dataValida = False

if 1 <= mes <= 12:
    if 1 <= dia <= diasMes[mes]:
        dataValida = True

if dataValida:
    print("Data Válida!")
else:
    print("Data Inválida")
