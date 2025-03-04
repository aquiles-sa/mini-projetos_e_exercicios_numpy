'''
Dado o array: arr = np.array([12, 25, 37, 42, 55]), 
como utilizar np.where para encontrar os índices dos elementos que são maiores que 30?
'''
import numpy as np

arr = np.array([12, 25, 37, 42, 55])

maiores_que_30 = lambda array: print(np.where(array > 30))
maiores_que_30(arr)