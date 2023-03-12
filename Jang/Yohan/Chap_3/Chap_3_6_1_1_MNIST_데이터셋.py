import sys, os
sys.path.append(os.pardir) # 부모 디렉터리의 파일을 가져올 수 있도록 설정
from dataset.mnist import load_mnist
# 처음 한 번은 몇 분 정도 걸립니다.
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력
print(x_train.shape) #
print(t_train.shape) #
print(x_test.shape) #
print(t_test.shape) #
(60000, 784)
(60000,)
(10000, 784)
(10000,)

# normalize = 0.0 에서 1.0 사이의 값으로 정규화 할 건지 
# False 는 0~255 값으로 그대로 출력

# flatten = 1 차원 배열로 만들건지
# false 는 1 x 28 x 28 의 3차원 배열로 
# true 는 784 개의 원소로 이뤄진 1차원 배열로 저장