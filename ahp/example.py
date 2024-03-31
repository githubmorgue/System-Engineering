import numpy as np
from ahp import AHP



# 准则重要性矩阵
criteria = np.array([
        [1, 1 / 3, 1 / 5], 
        [3, 1, 1 / 3], 
        [5, 3, 1]])

# 对每个准则，方案优劣排序
b1 = np.array([
        [1, 1/5, 1/7, 2, 5], 
        [5, 1, 1 / 2, 6, 8], 
        [7, 2, 1, 7, 9],
        [1/2, 1/6, 1/7, 1, 4],
        [1/5, 1/8, 1/9, 1/4, 1]])

b2 = np.array([
        [1, 1/3, 2, 1/5, 3], 
        [3, 1, 4, 1/7, 7], 
        [1/2, 1/4, 1, 1/9, 2],
        [5, 7, 9, 1, 9],
        [1/3, 1/7, 1/2, 1/9, 1]])

b3 = np.array([
        [1, 2, 4, 1/9, 1/2], 
        [1/2, 1, 3, 1/6, 1/3], 
        [1/4, 1/3, 1, 1/9, 1/7],
        [9, 6, 9, 1, 3],
        [2, 3, 7, 1/3, 1]])



b = [b1, b2, b3]
a = AHP(criteria, b).run()