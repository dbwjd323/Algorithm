n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
result = -1  # 전역 변수 result 초기화

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(current):
    global result  # 전역 변수를 사용하기 위해 선언
    if current == b:
        result = visited[current]  # 결과를 전역 변수로 저장
        return
    
    for i in graph[current]:
        if visited[i] == -1:
            visited[i] = visited[current] + 1
            dfs(i)

visited[a] = 0  # 시작점 a 방문 처리
dfs(a)
print(result)  # 경로가 없으면 -1 그대로 출력
