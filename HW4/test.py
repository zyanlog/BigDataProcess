#!/usr/bin/python3
import numpy as np

t_array = [[[1, 1, 1],[2, 2, 2]],[[1, 1, 1],[2, 2, 2]]]
array = np.array(t_array, float)
t_single = [[1, 1, 1],[2, 2, 2]]
single = np.array(t_single, float)

test = np.tile(single, (2, 1, 1))

print(array)
print(array.shape)
print(single)
print(single.shape)
print(test)
print(test.shape)
