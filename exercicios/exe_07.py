'''
Dado o array: arr = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36]]),
como obter todos os elementos da terceira coluna?
'''
import numpy as np

arr = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36]])
print(arr, end="\n\n")
print(arr[:3, 2])