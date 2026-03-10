tamanhoArquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidadeInternet = float(input("Informe a velocidade do link de internet (em Mbps): "))

velocidadeMBps = velocidadeInternet / 8

tempoSegundos = tamanhoArquivo / velocidadeMBps

tempoMinutos = tempoSegundos / 60

print(f"Tempo aproximado para instalar: {tempoMinutos:.2f} minuto(s)")