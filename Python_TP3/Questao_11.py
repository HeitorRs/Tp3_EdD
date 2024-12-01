def fatorial(n):
    print(f"Calculando fatorial({n})")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

#try:
#    print(fatorial(1000))
#except RecursionError as e:
#    print("Erro de recursão detectado!")

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial_iterativo(1000))
