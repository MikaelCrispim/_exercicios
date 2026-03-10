areaInformada = float(input("Informe o tamanho da área a ser pintada (em m²): "))

areaComFolga = areaInformada * 1.10
litrosNecessarios = areaComFolga / 6

apenasLatas = int(litrosNecessarios // 18)
if litrosNecessarios % 18 > 0: 
    apenasLatas += 1
precoLatas = apenasLatas * 80.00

apenasGaloes = int(litrosNecessarios // 3.6)
if litrosNecessarios % 3.6 > 0: 
    apenasGaloes += 1

precoGaloes = apenasGaloes * 25.00

latasMix = int(litrosNecessarios // 18)       
litrosRestantes = litrosNecessarios % 18      

galoesMix = int(litrosRestantes // 3.6) 
if litrosRestantes % 3.6 > 0:            
    galoesMix += 1

# 4 galoes = 100$ e 1 lata = 80$
if (galoesMix * 25) > 80:
    latasMix += 1
    galoesMix = 0

precoMix = (latasMix * 80.00) + (galoesMix * 25.00)

print(f"Só Latas: {apenasLatas} lata(s) R$ {precoLatas:.2f}")
print(f"Só Galões: {apenasGaloes} galão(ões) R$ {precoGaloes:.2f}")
print(f"Melhor Custo: {latasMix} lata(s) e {galoesMix} galão(ões) R$ {precoMix:.2f}")