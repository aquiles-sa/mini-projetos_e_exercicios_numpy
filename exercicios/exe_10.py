'''
Dado o array: arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]]),
como acessar os elementos da diagonal [5, 25, 45] utilizando listas de índices?
'''
import numpy as np

arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr, end="\n\n")

elementos_diagonal = arr.diagonal()
print(elementos_diagonal)

'''
elementos_diagonal = []

for i in range(0, len(arr)):
    elementos_diagonal.append(arr[i][i])

print(elementos_diagonal)
'''