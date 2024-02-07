# Dicionário com os valores de faturamento por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total mensal
total_mensal = sum(faturamento_por_estado.values())

# Calcular o percentual de representação de cada estado
percentuais_por_estado = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_por_estado.items()}

# Imprimir os resultados
print("Percentual de representação de cada estado no faturamento mensal:")
for estado, percentual in percentuais_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
