x = 0
def calcular(x):
    while x != 12:
        x = int(input("Informe um número cujo o mesmo somado ao seu dobro resulta em 36: "))
        result = 3 * x
        if result == 36:
            print("Você acertou! \nx * 3 = 36 \nx = 12!")
            break
print(calcular(x))