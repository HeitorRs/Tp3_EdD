def contar_repeticoes(string, caractere):
    string = string.lower()
    caractere = caractere.lower()
    if not string:
        return 0

    if string[0] == caractere:
        return 1 + contar_repeticoes(string[1:], caractere)
    else:
        return contar_repeticoes(string[1:], caractere)

palavra = "Anagrama"
caracter = "a"
resultado = contar_repeticoes(palavra, caracter)
print(f"O caractere '{caracter}' aparece {resultado} vezes na string '{palavra}'.")