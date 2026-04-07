min = int() 

while min < 1 or min > 99:  
    print("O valor min/max está fora dos parametros")
    min = int(input("Defina um valor minimo para a quantidade de strings entre 1 e 99: "))

max = int(input("Defina um valor máximo maior que o número mínimo e menor ou igual a 100: "))

def validarString(text):
        global min 
        global max

        tamanhoTexto = len(text)
        qtdValida = max - min

        if tamanhoTexto <= qtdValida:
            return True
        else:
            return False
text = "Teste"

if max > 100:
    print("O valor excedeu o limite")
else:
    print(validarString(text))
