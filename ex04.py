faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53,
}
total_faturamento = sum(faturamento.values())

percentual_por_estado = {}
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    percentual_por_estado[estado] = round(percentual, 2)

for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual: .2f}%")
