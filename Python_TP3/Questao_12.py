def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

lista = [1, 2, 3, 4, 5, 8, 4, 5, 3.5, 1.75]
resultado = soma_recursiva(lista)
print(f"A soma dos elementos é: {resultado}")