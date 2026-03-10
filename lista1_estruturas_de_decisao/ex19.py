numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

number = []

if centenas > 0:
    termo = "centena" if centenas == 1 else "centenas"
    number.append(f"{centenas} {termo}")

if dezenas > 0:
    termo = "dezena" if dezenas == 1 else "dezenas"
    number.append(f"{dezenas} {termo}")

if unidades > 0:
    termo = "unidade" if unidades == 1 else "unidades"
    number.append(f"{unidades} {termo}")

if len(number) == 3:
    resultado = f"{number[0]}, {number[1]} e {number[2]}"
elif len(number) == 2:
    resultado = f"{number[0]} e {number[1]}"
elif len(number) == 1:
    resultado = number[0]
else:
    resultado = "0 unidades"

print(f"Resultado: {resultado}")
