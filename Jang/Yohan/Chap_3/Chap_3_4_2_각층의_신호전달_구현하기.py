import numpy as np
import matplotlib.pyplot as plt
from Yohan.Chap_3.Chap_3_2_4_sigmoidFunction import sigmoid

# 3층 신경망

# 각 층의 신호 전달 구현하기

X = np.array([1.0, 0.5])  # (2,)  -> 열백터 // 행백터는 ([[1.0 , 0.5]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) # (2, 3)
B1 = np.array([0.1, 0.2, 0.3]) # (3,)

# 형상 2 * (2 x 3) + B1
A1 = np.dot(X, W1) + B1
Z1 =  sigmoid(A1)

print(A1) # [0.3 0.7 1.1]
print(Z1) # [0.57444252 0.66818777 0.75026011]

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print(Z1.shape) # (3,)
print(W2.shape) # (3, 2)
print(B2.shape) # (2,)
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 활성화 함수
'''
출력층의 활성화 함수는 풀고자 하는 문제의 성질에 맞게 정한다. 
예를 들어 회귀에는 항등 함수를 2클래스 분류에는 시그모이드 함수를, 
다중 클래스 분류에는 소프트맥스 함수를 사용하는 것이 일반적이다. 
'''

# 항등 함수
def identity_function(x):
    return x


W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3

Y = identity_function(A3) # 혹은 Y = A3




#  구현정리

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [ 0.31682708 0.69627909]
