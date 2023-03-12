import numpy as np
import matplotlib.pylab as plt


# 교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    # 1e-7 = 0.0000001
    return -np.sum(t * np.log(y + delta))
    '''
    numpy.log() = 밑이 e(자연 상수)인 log

    numpy.log2() = 밑이 2인 log

    numpy.log10() = 밑이 10인 log
    '''

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

a = cross_entropy_error(np.array(y), np.array(t))
print(a)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

b =  cross_entropy_error(np.array(y), np.array(t))
print(b)

# t가 0 -> 정답이 아닐 떄는 어차피 다 0값이 됨
# 3번쨰 값이 정답일 확률이 0.6인데 이떄의 오차율이 0,5
# 2번쨰 y 값은 정답 확률이 0.1 오차율은 2.3 으로 됨