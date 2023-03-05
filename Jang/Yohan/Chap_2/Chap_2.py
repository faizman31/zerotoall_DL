import numpy as np
import matplotlib.pyplot as plt

# AND 함수 
def AND(x1, x2):
    w1, w2, theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
print("")
print("---------------------")
print("AND 함수")
print("---------------------")
print("AND 함수 기대값 0 출력" , AND(0,0))
print("AND 함수 기대값 0 출력" , AND(1,0))
print("AND 함수 기대값 0 출력" , AND(0,1))
print("AND 함수 기대값 1 출력" , AND(1,1))
print("")

############################

# 가중치와 편향 도입


x = np.array([0, 1 ]) # 입력
w = np.array([0.5, 0.5]) # 가중치
b = -0,7 # 편향

print("")
print("---------------------")
print("가중치와 편향 도입")
print("---------------------")
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)
print("")

#############################

# 가중치와 편향 구현하기

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7 # theta -> -b 로 변경
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

###########################

# NAND 게이트 + OR 게이트

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # and와는 가중치(w와 b)만 다르다!
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # and와는 가중치(w와 b)만 다르다!
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
############################

# XOR 은 00 , 11 은 0 / 하나라도 1 이면 1
# AND 는 11 빼고 나머지 0 ->      1,0 , 0,1 , 0,0  -> 0 / 1,1  -> 1
# NAND 는 11 빼고 나머지 1        1,0 , 0,1 , 0,0  -> 1 / 1,1  -> 0
# OR 은 00 빼고 나머지 1          1,0 , 0,1 , 1,1  -> 1 / 0,0  -> 0

# AND 와 OR 조합 -> NAND로 출력 -> XOR 구현


###############################

# XOR 게이트 구현하기

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print("")
print("---------------------")
print("XOR 게이트 구현하기")
print("---------------------")
print(XOR(0, 0), "-> 예상) 0 을 출력")
print(XOR(1, 0), "-> 예상) 1 을 출력")
print(XOR(0, 1), "-> 예상) 1 을 출력")
print(XOR(1, 1), "-> 예상) 0 을 출력")
print("")