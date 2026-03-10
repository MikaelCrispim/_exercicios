data = input("Informe uma data no formato ddmmaaaa (com ou sem barras): ")

meses = {
    "01":"Janeiro",
    "02":"Fevereiro",
    "03":"Março",
    "04":"Abril",
    "05":"Maio",
    "06":"Junho",
    "07":"Julho",
    "08":"Agosto",
    "09":"Setembro",
    "10":"Outubro",
    "11":"Novenbro",
    "12":"Dezembro"
}

mes = data[3:5]
if len(data) == 8 and data.isdigit():
    data = data[:2] + '/' + data[2:4] + '/' + data[4:]
    mes = data[3:5]
    if mes in meses:
        print(f"{data[:2]} de {meses[mes]} de {data[6:]}")
else:
    print(f"{data[:2]} de {meses[mes]} de {data[6:]}")
# print(data)