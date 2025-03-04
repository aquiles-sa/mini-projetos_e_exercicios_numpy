# Dado o array: arr = np.array([4, 9, 12, 15, 20, 25]), qual código retorna apenas os valores maiores que 10?
import numpy as np

arr = np.array([4, 9, 12, 15, 20, 25])
print(arr[arr > 10])