# Dado o array: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), como selecionar os elementos [5, 6, 8, 9] formando uma submatriz 2x2?

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr, end="\n\n")

submatriz = arr[1:, 1:]
print(submatriz)

'''
matriz_atualizada = arr[::1][1:]
primeira_parte = matriz_atualizada[0][1::]
segunda_parte = matriz_atualizada[1][1::]

matriz_elementos = np.concat((primeira_parte, segunda_parte), axis=None).reshape(2, 2)
print(matriz_elementos)
'''