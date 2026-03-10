a = int(input("Informe o valor de A:"))
if a == 0:
    print("Programa finalizado")
else:
    b = int(input("Informe o valor de B:"))
    c = int(input("Informe o valor de C:"))

    delta = (b**2) - ((4*a)*c)

    if delta < 0:
        print("Não tem raízes")
    elif delta == 0:
        x = (-b + delta) / 2*a
        
        print(f"A raiz é {x}")
    else:           # raiz quadrada de um numero é a mesma coisa que elevar o numero a 1/2
        x1 = (-b + (delta ** 0.5))/2*a 
        x2 = (-b - (delta ** 0.5))/2*a

        print(f"As raízes são: {x1} e {x2}")