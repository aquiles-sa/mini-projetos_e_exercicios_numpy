# Dado o array: arr = np.array([2, 4, 6, 8, 10]), como alterar todos os elementos pares para -1 usando indexação booleana?
import numpy as np

arr = np.array([2, 4, 6, 8, 10])
pares = arr % 2 == 0
arr[pares] = -1

print(arr)