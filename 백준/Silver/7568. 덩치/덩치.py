import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    weight, height = sys.stdin.readline().split()
    arr.append([int(weight), int(height)])

# 덩치 배열
rank_arr = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue #자신과 자신을 비교하는 경우는 넘어간다
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: 
            rank = rank + 1
    
    rank_arr.append(rank)

print(" ".join(map(str, rank_arr)))