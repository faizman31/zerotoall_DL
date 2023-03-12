import numpy as np
import matplotlib.pylab as plt
from Chap_4_3_1_미분 import numerical_diff 

# 수치 미분의 예 
# y = 0.01x^2 + 0.1x
def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0, 20.0, 0.1) # 0에서 20까지 0.1 간격의 배열 x를 만든다(20은 미포함).
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

a = numerical_diff(function_1, 5)
print(a)