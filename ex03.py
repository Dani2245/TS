import json

with open("dados.json") as meu_json:
    dados_json = json.load(meu_json)


def menor_faturamento(dados):
    valor_minimo = 0
    for item in dados:
        if item["valor"] != 0.0 or item["valor"] < valor_minimo:
            valor_minimo = item["valor"]
    print(f"O menor valor de faturamento é : R$ {valor_minimo}")
    return valor_minimo


def maior_faturamento(dados):
    valor_maximo = 0
    for item in dados:
        if item["valor"] != 0 and item["valor"] > valor_maximo:
            valor_maximo = item["valor"]
    print(f"O maior valor de faturamento é : R$ {valor_maximo}")
    return valor_maximo


def media_faturamento(dados):
    faturamento = 0
    contador_dias = 0
    n_dias_maior_media = 0
    for item in dados:
        if item["valor"] != 0.0:
            faturamento = faturamento + item["valor"]
            contador_dias = contador_dias + 1
    media = faturamento / contador_dias
    media_formatada = "{:.4f}".format(media)

    for item in dados:
        if item["valor"] > media:
            n_dias_maior_media = n_dias_maior_media + 1

    print(f"A média de faturamento é : R$ {media_formatada}")
    print(f"{n_dias_maior_media} dias no mês teve o faturamento maior que a média")
    return n_dias_maior_media


menor_faturamento(dados_json)
maior_faturamento(dados_json)
media_faturamento(dados_json)
