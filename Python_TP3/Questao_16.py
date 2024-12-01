def inverter_string(string):
    if len(string) <= 1:
        return string

    return string[-1] + inverter_string(string[:-1])

resultado = inverter_string("Recursao")
print(f"A string invertida é: {resultado}")