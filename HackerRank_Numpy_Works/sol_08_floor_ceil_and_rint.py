import numpy as np
np.set_printoptions(legacy='1.13')

i = np.array(list(map(float, input().split())), float)

print(np.floor(i))
print(np.ceil(i))
print(np.rint(i))
