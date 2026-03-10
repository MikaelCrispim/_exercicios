palavraNormal = "embaralhada"
listaPalavra = list(palavraNormal)
alea = 1
for i in range(1, len(listaPalavra), 2):
    listaPalavra[i] = listaPalavra[alea]
tentativa = ""
palavraFinal = ("".join(listaPalavra))
while tentativa != palavraNormal:
    print(f"A palavra embaralhada é: {palavraFinal}")
    tentativa = input("Tente acertar a palavra: ").lower()
    if tentativa == palavraNormal:
        print(f"Parabéns, você acertou!")