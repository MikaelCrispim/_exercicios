numero = input("Insira um numero até 99: ")

dezenas = {
        "2": "Vinte",
        "3": "Trinta",
        "4": "Quarenta",
        "5": "Cinquenta",
        "6": "Sessenta",
        "7": "Setenta",
        "8": "Oitenta",
        "9": "Noventa"
    }
unidades = {
        "0": "Zero",
        "1": "Um",
        "2": "Dois",
        "3": "Três",
        "4": "Quatro",
        "5": "Cinco",
        "6": "Seis",
        "7": "Sete",
        "8": "Oito",
        "9": "Nove"
    }
especiais = {
        "10": "Dez",
        "11": "Onze",
        "12": "Doze",
        "13": "Treze",
        "14": "Quatorze",
        "15": "Quinze",
        "16": "Dezesseis",
        "17": "Dezessete",
        "18": "Dezoito",
        "19": "Dezenove"
    }

if len(numero) == 2 and numero[0] == "0":
    numero = numero[1]

if numero in especiais:
    print(especiais[numero])
    
elif len(numero) == 2:
    if numero[1] == "0":
        print(dezenas[numero[0]])
    else:
        print(f"{dezenas[numero[0]]} e {unidades[numero[1]].lower()}")
        
elif len(numero) == 1:
    if numero in unidades:
        print(unidades[numero])
else:
    print("Número fora do intervalo permitido (0 a 99).")