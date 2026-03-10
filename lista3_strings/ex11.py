# jogo da forca - Mikael Crispim
import random

palavras = ['SQL', 'PYTHON', 'JAVA', 'JAVASCRIPT', 'HTML', 'CSS', 'PHP']
palavraEscolhida = random.choice(palavras)

palavraAcertada = ["_"] * len(palavraEscolhida)

pontuacao = 0

while pontuacao != len(palavraEscolhida):
    
    print(" ".join(palavraAcertada))

    tentativa = input("Jogo da Forca: (Escolha uma letra e verique se a mesma contém na palavra): ").upper()

    if tentativa in palavraEscolhida:

        # Passo por todas as letras da palavra
        for i in range(len(palavraEscolhida)):
            # Vejo se a posiçao do contador é igual a letra da minha tentativa 
            if palavraEscolhida[i] == tentativa:
            # Verifico se a posição da letra não foi preenchida 
              if palavraAcertada[i] == "_":
                  palavraAcertada[i] = tentativa
                  pontuacao += 1  
                # Volto para o loop e verifico novamente para calcular as letras repetidas
    else:
        print("Incorreto")
        
print(f"Parabéns, a palavra era: {" ".join(palavraAcertada)}")
