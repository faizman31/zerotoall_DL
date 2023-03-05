import numpy as np
import matplotlib.pyplot as plt

# 계단 함수 구현
def step_function(x):
    if x > 0:
        return 1
    else: 
        return 0
    

X = np.array([-1.0, 1.0, 2.0])

y = X > 0
print(y) # -> [False, True, True]

y = y.astype(np.intc)
print(y) # -> y의 bool 값 -> True 면 1 False 면 0 로 변환해줌



# 계단 함수의 그래프
def step_function(x):
    return np.array(x>0, dtype=np.intc)

# -5.0 부터 5.0 전까지 0.1 간격으로 배열 생성
# -> [-5.0,-4.9,.....,4.9]
x = np.arange(-5.0, 5.0, 0.1) 


y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y축의 범위 지정
plt.show()
