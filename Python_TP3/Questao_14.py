def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

lista = [11, 2, 32, 4, 5, 8, 4, 5]
resultado = soma_recursiva(lista)
print(f"A soma dos elementos é: {resultado}")