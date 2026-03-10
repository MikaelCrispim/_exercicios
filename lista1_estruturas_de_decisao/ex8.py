produtos = {
    'Apple':0,
    'Samsung':0,
    'Xiaomi':0
    }    

for chave, values in produtos.items():
    values = float(input("Insira o preço do celular " + chave + ": "))
    produtos[chave] = values

maisBarato = min(produtos, key=produtos.get)

print(produtos)
print(f"Você deve comprar o celular {maisBarato} !")