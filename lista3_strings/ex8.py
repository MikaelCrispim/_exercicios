def isPalindrome(s):
    esquerda = 0 
    direita = len(s) - 1
    
    while esquerda < direita:
        # Pula campos vazios
        if not s[esquerda].isalnum():
            esquerda += 1
        # Pula campos vazios
        elif not s[direita].isalnum():
            direita -= 1
        # Compara os dois 
        else:
            # se forem diferentes, False
            if s[esquerda].lower() != s[direita].lower():
                return False
            # Se não continue a contagem dos ponteiros
            esquerda += 1
            direita -= 1
            
    return True

s = input("Insira a palavra para verificar se é um palindromo")
print(isPalindrome(s))