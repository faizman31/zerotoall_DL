
import numpy as np
from Chap_4_4_0_기울기 import numerical_gradient
# 경사하강법
# f sms 최적화 하려는 함수
# init_x 는 초깃값
# lr 은 learning late를 의미하는 학습률
# step_num 경사법에 따른 반복 횟수를 뜻함

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

# 경사하강법으로 f(x[0],f[1]) = x[0]^2 + x[1]^2 의 최솟값을 구하여라

def function_2(x):
    return x[0]**2 + x[1]**2
init_x = np.array([-3.0, 4.0])
a = gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)
print(a)
# array([ -6.11110793e-10, 8.14814391e-10])




# 학습률이 너무 큰 예 : lr = 10.0
init_x = np.array([-3.0, 4.0])
a = gradient_descent(function_2, init_x= init_x, lr=10.0, step_num=100)
print(a)
# array([ -2.58983747e+13, —1.29524862e+12])




# 학습률이 너무 작은 예 : lr = 1e-10
init_x = np.array([-3.0, 4.0])
a = gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100)

print(a)
# array([-2.99999994, 3.99999992])
