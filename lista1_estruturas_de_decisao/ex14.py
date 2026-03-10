notas = []
for i in range(2):
    nota = float(input("Insira as suas notas: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 9.01 or media <= 10:
    conceito = 'A'
    msg = 'Aprovado'
elif media >= 7.51 or media <= 9:
    conceito = 'B'
    msg = 'Aprovado'
elif media >= 6.01 or media <= 7.5:
    conceito = 'C'
    msg = 'Aprovado'
elif media >= 4.01 or media <= 6:
    conceito = 'D'
    msg = 'Reprovado'
else:
    conceito = 'E'
    msg = 'Reprovado'

print(f'''
    Suas notas foram {notas}
    Sua média foi {media}
    Seu conceito foi {conceito}
    Você foi: {msg}
      ''')