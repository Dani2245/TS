def inversor_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]

    print(f"Texto original: {texto}")
    print(f"Texto invertido: {texto_invertido}")
    return texto_invertido


inversor_string("A semana inteira fiquei esperando")
