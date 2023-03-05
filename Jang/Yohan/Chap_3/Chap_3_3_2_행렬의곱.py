import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],[3,4]])

B = np.array([[3,1],[4,2]])

# 내적 -> 결과 값이 스칼라
# 행렬의 곱은 B A / A B 곱하는 순서에 따라 값이 달라짐
print(f'헹렬의 곱 : {np.dot(A,B)}')

# 행렬의 곱-> 3차원 부터는 텐서 곱(외적)을 하게되어 방식이 달라짐
print(f'헹렬의 곱 : {A@B}')

# 스칼라 곱 (shape가 같아야 함)
print(f'헹렬의 곱 : {A*B}')


# 행렬의 곱은 차원의 원소수가 일치해야함 
# A = 3 x 2    B = 2        ->  3
# A = 5 x 4    B = 4 x 3    -> 5 x 3