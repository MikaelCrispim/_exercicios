x = 0.0
def calcular(x):
    while x != 4.5:
        x = float(input("Informe um número que multiplicado por 3 e subtraído por 9 seja igual a ele mesmo: "))
        answer = (x * 3) - 9
        if answer == x:
            print("Você acertou!")
            break
print(calcular(x))