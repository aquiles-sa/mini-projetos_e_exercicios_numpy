# Com base no mesmo array (arr), como acessar o último elemento da primeira linha usando indexação negativa?
import numpy as np

arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])

print(arr, end="\n\n")
print(arr[0, -1])