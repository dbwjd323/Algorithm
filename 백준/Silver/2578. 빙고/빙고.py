# 철수의 빙고판 입력
c = [list(map(int, input().split())) for _ in range(5)]

# 사회자 입력
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def check(c):
    bingo = 0
    # 가로 체크
    for i in c:
        if i.count(0) == 5:
            bingo += 1

    # 세로 체크
    for i in range(5):
        count = 0
        for j in range(5):
            if c[j][i] == 0:
                count += 1
        if count == 5:
            bingo += 1

    # 왼쪽 대각선 체크
    count = 0
    for i in range(5):
        if c[i][i] == 0:
            count += 1
    if count == 5:
        bingo += 1

    # 오른쪽 대각선 체크
    count = 0
    for i in range(5):
        if c[i][4 - i] == 0:
            count += 1
    if count == 5:
        bingo += 1

    return bingo

# 빙고가 될 수 있는 최소의 숫자 수는 12개다
n = 0
for i in range(25):
    # 사회자가 부른 숫자를 철수의 빙고판에서 찾아 0으로 변경
    for j in range(5):
        for k in range(5):
            if mc[i] == c[j][k]:
                c[j][k] = 0
                n += 1
                
    # 빙고 줄 수 확인
    if check(c) >= 3:
        print(n)
        break
