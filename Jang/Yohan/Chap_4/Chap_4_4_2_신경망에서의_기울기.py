import numpy as np
from Chap_4_4_0_기울기 import numerical_gradient as up


# 신경망에서의 기울기
import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화
        self.Z = 1
        
    def predict(self,x):
        return np.dot(x, self.W)
    # 행렬의 곱
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

net = simpleNet()

# print(f"This is test : {net.Z}")
# print(net.Z)

X = np.array([0.6, 0.9])
p = net.predict(X)

print(np.argmax(p)) # 최댓값의 인덱스


t = np.array([0, 0, 1]) # 정답 레이블

print(net.loss(X, t))


def f(W): # 왜 더미지? # -> 이부분 다시 확실히 알아볼 것
    
    return net.loss(X, t)

dW = numerical_gradient(f, net.W)

print(dW)


