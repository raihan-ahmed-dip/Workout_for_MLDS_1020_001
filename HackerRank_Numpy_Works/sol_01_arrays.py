import numpy as np

def arrays(arr):
    a = np.array(arr, dtype=float)
    a = np.flip(a)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
