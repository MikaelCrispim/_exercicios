texto = input("Informe um texto para converter em Leet Speak: ")

texto = texto.replace("A", "4").replace("a", "4")
texto = texto.replace("E", "3").replace("e", "3")
texto = texto.replace("I", "1").replace("i", "1")
texto = texto.replace("O", "0").replace("o", "0")
texto = texto.replace("S", "5").replace("s", "5")
texto = texto.replace("T", "7").replace("t", "7")

print(f"Texto em Leet: {texto}")