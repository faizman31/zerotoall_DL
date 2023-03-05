import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 구현하기

def sigmoid(x):
    return 1/ (1+np.exp(-x))
    


# 시그모이드 함수 그리기

# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) #y축 범위 지정
# plt.show()

