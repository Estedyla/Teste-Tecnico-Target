import json

def carrega_faturamento_json(caminho):
    with open(caminho) as f:
        faturamento_diario = json.load(f)
    return faturamento_diario

def calcular_estatisticas_faturamento(faturamento_diario):
    dias_com_faturamento = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    return menor_valor, maior_valor, dias_acima_media

if __name__ == "__main__":
    # Carregar dados de faturamento do arquivo JSON
    faturamento_diario = carrega_faturamento_json('dados.json')

    # Calcular estatísticas de faturamento
    menor_valor, maior_valor, dias_acima_media = calcular_estatisticas_faturamento(faturamento_diario)

    # Imprimir resultados
    print("Menor valor de faturamento:", menor_valor)
    print("Maior valor de faturamento:", maior_valor)
    print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
