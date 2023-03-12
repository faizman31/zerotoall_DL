import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000z 10)


train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
# 이전 배치는 스텝이였는데 이번 배치는 10개를 무작위로 뽑는거임

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
