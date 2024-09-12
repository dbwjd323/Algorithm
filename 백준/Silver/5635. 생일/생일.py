#학생 수를 입력받음
N = int(input())

arr = []
for _ in range(N):
    name, d, m, y = input().split()
    d,m,y = map(int,(d,m,y))
    arr.append((y, m, d, name))
    
#년도가 낮은 순으로 정렬
arr.sort()

print(arr[-1][3])
print(arr[0][3])