
from Chap_4_3_1_미분 import numerical_diff 


# 편미분

# f(x0 , x1) = x0^2 + x1^2
def function_2(x):
    return x[0]**2 + x[1]**2
    # 또는 return np.sum(x**2)
    
# 문제1 :  x[0] = 3 x[1] = 4 일때 x[0]에 대한 편미분을 구하라


def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

a = numerical_diff(function_tmp1, 3.0)
print(a)

# 문제2 :  x[0] = 3 x[1] = 4 일때 x[1]에 대한 편미분을 구하라

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

a = numerical_diff(function_tmp2, 4.0)

print(a)

