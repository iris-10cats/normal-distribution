import numpy as np
rng = np.random.default_rng()
numbers = rng.normal(loc= 6, scale = 3, size=708)
rounded_numbers = np.around(numbers, decimals=1)
rounded_numbers2 = np.around(rounded_numbers*2)/2
my_rounded_list = [rounded_numbers2]
import os
print(os.getcwd())
import sys
with open('filename.txt', 'w') as f:
    print(my_rounded_list, file=f)