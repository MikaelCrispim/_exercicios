str1 = input("Digite qualquer coisa: ")
str2 = input("Digite qualquer coisa: ")

size = "sim" if len(str1) == len(str2) else "não"
content = "sim" if str1 == str2 else "não"

print(f'''
      O contéudo das strings é: {str1} e {str2} 
      O tamanho das strings : {len(str1)} e {len(str2)}
      Possuem o mesmo tamanho: {size}
      Possuem o mesmo conteúdo: {content}
    ''')
