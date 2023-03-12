import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

# 배치용 교차 엔트로피 오차 구현하기

def cross_entropy_error(y, t):
    if y.ndim == 1:
        # ndim 은 y 의 차원의 수, 배열의 축 수
        # t는 정답테이블
        # y는 신경망 출력
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size
# 1e-7 = 0.0000001


# 이해안감.
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        batch_size = y.shape[0]
        # 배치 사이즈가 5라면 np.arrange(5) 는 [0,1,2,3,4] 라는 넘파이 배열
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


'''

reshape는 배열 변환 ->
a = [1,2,3,4,5,6,7,8]
b = np.reshape(a,(2,4))
c = np.reshape(a,(4,2))

[[1 2 3 4]
 [5 6 7 8]]
 
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
 
print(b.shape[0])
print(b.shape[1])

2
4
'''
