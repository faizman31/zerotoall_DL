import numpy as np
import matplotlib.pyplot as plt

# def softmax(a):  -> 값이 크면 오버플로 발생
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#     return y



# 출력이 0 에서 1 사이의 실수
# 총 출력의 합은 1 -> 확률로 해석 가능 -> 통계적으로 대응 가능
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a= np.array([0.3,2.9,4.0])
y = softmax(a)

print(np.sum(y))