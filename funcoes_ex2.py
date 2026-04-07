taxa = float(input("Qual é a taxa de imposto: "))
produtoPreco = float(input("Qual é o valor do produto: "))

def somaImposto(taxa, produtoPreco):
    valorFinal = ((taxa / 100) + 1) * produtoPreco
    print(f"O valor total do produto é: {valorFinal:.2f}")
    
somaImposto(taxa,produtoPreco)