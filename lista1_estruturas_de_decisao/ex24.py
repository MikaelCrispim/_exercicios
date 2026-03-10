n1 = float(input("Informe o primeiro número "))
n2 = float(input("Informe o segundo número "))
operacao = input("Informe a operação desejada: (+, -, *, d)")

match operacao:
    case '+':
        resultado = n1 + n2
        print(resultado)
    case '-':
        resultado = n1 - n2
        print(resultado)
    case '*':
        resultado = n1 * n2
        print(resultado)
    case 'd':
        resultado = n1 / n2
        print(resultado)
    case _:
        print("Operação inválida")


if resultado % 2 == 0:
    print("é par")
else:
    print("é impar")

if resultado >= 0:
    print("é positivo")
else:
    print("é negativo")

if resultado != round(resultado):
    print("é decimal")
else:
    print("é inteiro")