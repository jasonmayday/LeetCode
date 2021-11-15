import time 
import numpy as np

a = np.random.uniform (size = (500, 500))

s_time = time.time()

for i in range(100):
    a += 1
    np.linalg.svd(a)

print(time.time() - s_time)