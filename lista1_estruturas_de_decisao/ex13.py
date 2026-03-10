dias = {
    1:'Domingo',
    2:'Segunda',
    3:'Terça',
    4:'Quarta',
    5:'Quinta',
    6:'Sexta',
    7:'Sábado'
}

dia = int(input("Digite um número de 1 a 7 para verificar o dia correspondente da semana: "))

if dia in dias:
    print(dias[dia])
else:
    print("Valor inválido!") 