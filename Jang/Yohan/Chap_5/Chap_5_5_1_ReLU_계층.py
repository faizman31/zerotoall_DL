import numpy as np

class Relu:
    def __init__(self):
        self.mask = None
    def forward(self, x):
        
        self.mask = (x <= 0) # mask에 true false로 저장됨
        out = x.copy() # out은 원래 값
        out[self.mask] = 0
        return out
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

x = np.array( [[1.0, -0.5], [-2.0, 3.0]] )
print(x)
# [[ 1. -0.5]
# [-2. 3. ]]

# relu = Relu()
# print(relu.forward(x)) 


mask = (x <= 0)


print(mask)
# [[False True]
# [ True False]]
