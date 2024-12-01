def verificar_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    
    if palavra[0] != palavra[-1]:
        return False

    return verificar_palindromo(palavra[1:-1])

palavras = ["amor", "radar", "ovo"]
for palavra in palavras:
    if verificar_palindromo(palavra):
        print(f'A palavra "{palavra}" é um palíndromo.')
    else:
        print(f'A palavra "{palavra}" não é um palíndromo.')