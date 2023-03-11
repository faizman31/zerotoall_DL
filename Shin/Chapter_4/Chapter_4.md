# Chapter 4. 신경망 학습  

## 4.1 데이터에서 학습한다!
- 신경망의 특징 : 데이터를 보고 학습 -> **가중치 매개변수**의 값을 데이터를 보고 자동으로 결정  

### 4.1.1 데이터 주도 학습
- 기계학습에 생명 -> "데이터"
- 데이터에서 답을 찾고 패턴을 발견하고 데이터로 이야기를 만드는 것이 기계학습이다.
- 특징(Feature) : 입력 데이터(입력 이미지)에서 본질적인 데이터(중요한 데이터)를 정확하게 추출할 수 있도록 설계된 변환기
- 신경망은 모든 문제를 주어진 데이터 그대로를 입력 데이터로 활용해 'End-to-End'로 학습이 가능하다.  

### 4.1.2 훈련 데이터와 학습 데이터
- 기계학습 문제는 데이터를 훈련 데이터(Training Data)와 시험 데이터(Test Data)로 나누어 학습/실험을 수행
- 왜 훈련데이터와 시험데이터를 나누어야 할까? -> **범용 능력**을 제대로 평가하기 위해
- 범용능력이란? : 아직 보지 못한 데이터(훈련 데이터에 포함되어 있지 않는 데이터)로도 문제를 올바르게 풀어내는 능력
- 오버피팅(Overfitting)이란? : 한 데이터셋에만 지나치게 최적화된 상태  

## 4.2 손실함수
- 신경망 학습에서는 현재 상태를 '하나의 지표'로 표현합니다.
- 신경망 학습은 '하나의 지표'를 가장 좋게 만들어주는 가중치 매개변수의 값을 탐색하는 것
- 신경망 학습의 '하나의 지표' -> **손실 함수(Loss function)**  
### 4.2.1 오차제곱합(Sum of Squares for error,SSE)
- 오차제곱합 수식
$$ E = {1 \over 2} \sum (y_k - t_k)^2
$$
- 원-핫 인코딩이란? : 한 원소만 1로 하고 그 외는 0으로 나타내는 표기법
### 4.2.2 교차 엔트로피(Cross Entropy error,CEE)
- 교차 엔트로피 오차(Cross Entropy error,CEE)의 수식
$$ -\sum{t_k\log{y_t}}
$$  
### 4.2.3 미니배치 학습 
- 데이터의 개수와 관계없이 언제든 통일된 지표를 얻고 싶다면? -> 데이터의 갯수 N으로 나눔으로써 **"평균 손실 함수"** 를 구하면 된다.
- 미니배치(mini-batch) 학습 : 많은 데이터를 대상으로 데이터 일부를 추려 전체의 '근사치'로 이용하는 방법으로 훈련 데이터로부터 일부만을 골라 학습을 수행