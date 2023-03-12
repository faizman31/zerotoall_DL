
# 미분

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

# 컴퓨터의 시스템적 한계 때문에 중위값을 구해서 해결