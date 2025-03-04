'''
Dado o array: arr = np.array([10, 20, 30, 40, 50]) e indices = [0, 2, 4],
como utilizar os índices da lista indices para acessar os elementos correspondentes de arr?
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]

print(arr[indices])

'''
for i in range(0, len(arr)):
    print(arr[indices])
    break
'''