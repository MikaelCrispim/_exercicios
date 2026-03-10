saque = int(input("Informe o valor do saque (Mín: R$ 10 | Máx: R$ 600): "))

if saque < 10 or saque > 600:
    print("Valor inválido para saque.")
else:
    valorRestante = saque
    
    notasDisponivel = [
        100, 
        50, 
        10, 
        5, 
        1
    ]
 
    for nota in notasDisponivel:
        quantidadeNotas = valorRestante // nota
        
        if quantidadeNotas > 0:
            valorRestante %= nota
            
            termo = "nota" if quantidadeNotas == 1 else "notas"
            print(f"- {quantidadeNotas} {termo} de R$ {nota}")
