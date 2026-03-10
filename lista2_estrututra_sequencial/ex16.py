tamanhoParede = float(input("Qual a área em M² que você deseja pintar "))
umaLataCobre = 54
custoLata = 80
quantidadeCheia = tamanhoParede // umaLataCobre
if tamanhoParede % umaLataCobre != 0:
    quantidadeCheia = quantidadeCheia + 1
    print(f"A quantidade necessária é: {quantidadeCheia:.0f} lata(s) e você vai gastar R${custoLata * quantidadeCheia}") 
else:
    print(f"A quantidade necessária é: {quantidadeCheia:.0f} lata(s) e você vai gastar R${custoLata * quantidadeCheia}") 