import numpy as np

qtd_alunos = 20
qtd_materias = 5

np.random.seed(42)
notas = np.random.uniform(0, 10, (qtd_alunos, qtd_materias))

materias = ["Matemática", "Física", "Química", "História", "Português"]

media_materia = np.mean(notas, axis=0)
mediana_materia = np.median(notas, axis=0)
maior_nota = np.max(notas, axis=0)
menor_nota = np.min(notas, axis=0)

print()
print("Dados das notas dos alunos: ", end="\n\n")

for i in range(qtd_materias):
    print(materias[i])
    print(f"Média: {round(media_materia[i], 2)}")
    print(f"Mediana: {round(mediana_materia[i], 2)}")
    print(f"Maior nota: {round(maior_nota[i], 2)}")
    print(f"Menor nota: {round(menor_nota[i], 2)}")
    print("-" * 20)
    
media_geral = np.mean(notas)
media_aluno = np.mean(notas, axis=1)
alunos_acima_media = 0
alunos_abaixo_media = 0

for media in media_aluno:
    if media > media_geral:
        alunos_acima_media += 1
    else:
        alunos_abaixo_media += 1

print()
print(f"Alunos acima da média: {alunos_acima_media}")
print(f"Alunos abaixo da média: {alunos_abaixo_media}")