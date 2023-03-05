import numpy as np
import matplotlib.pyplot as plt

# 다차원 배열

A = np.array([1,2,3,4])
print('--------------------------')
print(A)
print(f'A 배열의 차원 : {np.ndim(A)} 차원')
print(f'A 배열의 형상 : {np.shape(A)} <- 튜플형태')


B = np.array([[1,2],[3,4],[5,6]])
print('--------------------------')
print(B)
print(f'B 배열의 차원 : {np.ndim(B)} 차원')
print(f'B 배열의 형상 : {np.shape(B)} <- 튜플형태')