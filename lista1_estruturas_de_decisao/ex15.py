l1 = int(input("Insira um lado do triangulo: "))
l2 = int(input("Insira um lado do triangulo: "))
l3 = int(input("Insira um lado do triangulo: "))

if l1 == l2 and l2 == l3:
    tipoTriangulo = 'Triangulo Equilátero'
elif l1 == l2 or l1 == l3 or l2 == l3:
    tipoTriangulo = 'Triangulo Isósceles'
else:
    tipoTriangulo = 'Triangulo Escaleno'

print(tipoTriangulo)