T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    X, Y = A, B

    # GCD 계산 (유클리드 호제법)
    while Y != 0:
        X, Y = Y, X % Y

    # LCM 계산 및 출력
    print(A * B // X)  # X가 GCD, A * B // X가 LCM
    # // 연산은 정수 나눗셈 연산자
