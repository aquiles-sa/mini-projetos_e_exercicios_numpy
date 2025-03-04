import numpy as np

qtd_dias = 30

np.random.seed(42)
temperaturas = np.random.uniform(15, 40, qtd_dias)
umidades = np.random.uniform(15, 80, qtd_dias)
velocidade_ventos = np.random.uniform(5, 20, qtd_dias)

dados = np.array([temperaturas, umidades, velocidade_ventos])

print()
print("Estatísticas meteorológicas (30 dias): ")
print(f"Temperatura - Média: {round(temperaturas.mean(), 2)}°C | Máxima: {round(temperaturas.max(), 2)}°C | Mínima: {round(temperaturas.min(), 2)}°C")
print(f"Umidade - Média: {round(umidades.mean(), 2)}% | Máxima: {round(umidades.max(), 2)}% | Mínima: {round(umidades.min(), 2)}%")
print(f"Ventos - Média: {round(velocidade_ventos.mean(), 2)}km/h | Máxima: {round(velocidade_ventos.max(), 2)}km/h | Mínima: {round(velocidade_ventos.min(), 2)}km/h", end="\n\n")

dia_mais_quente = temperaturas.argmax() + 1
dia_mais_umido = umidades.argmax() + 1
dia_maior_vento = velocidade_ventos.argmax() + 1
dias_calor_secos = (temperaturas > 30) & (umidades < 50)

print(f"Dia mais quente - Dia: {dia_mais_quente} | Temperatura: {round(temperaturas.max(), 2)}°C")
print(f"Dia mais umido - Dia: {dia_mais_umido} | Umidade: {round(umidades.max(), 2)}%")
print(f"Dia com maior ventania - Dia: {dia_maior_vento} | Vento: {round(velocidade_ventos.max(), 2)}km/h")