import numpy as np

dias = 30

np.random.seed(42)

faturamento = np.random.uniform(100, 5000, dias)
media_faturamento = np.mean(faturamento)
mediana_faturamento = np.medin(faturamento)
desvio_padrao_faturamento = np.std(faturamento)

dia_mais_rentavel = faturamento.argmax() + 1
dia_menos_rentavel = faturamento.argmin() + 1

print()
print("Estatísticas de vendas durante um mês: ")
print(f"Média diária: R$ {round(media_faturamento, 2)}")
print(f"Mediana diária: R$ {round(mediana_faturamento, 2)}")
print(f"Desvio padrão: R$ {round(desvio_padrao_faturamento, 2)}")
print(f"Dia mais rentável: {dia_mais_rentavel}")
print(f"Dia menos rentável: {dia_menos_rentavel}")
print("-" * 40)

variacao_dias = np.diff(faturamento)
dias_crescimento = np.sum(variacao_dias > 0)
dias_queda = np.sum(variacao_dias < 0)

print("Tendência de faturamento: ")
print(f"Dias de crescimento: {dias_crescimento}")
print(f"Dias de queda: {dias_queda}")