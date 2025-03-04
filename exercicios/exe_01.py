# Dado o array (arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])), Qual código retorna a segunda e a terceira coluna da matriz? 
import numpy as np

arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(arr, end="\n\n")

print(arr[:, [2, 3]])