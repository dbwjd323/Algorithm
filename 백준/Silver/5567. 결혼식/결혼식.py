import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
    
graph = [[0]*(n+1) for _ in range(n+1)]  # 인접 행렬로 초기화
visited = [0 for _ in range(n+1)]  # 방문 여부 체크 리스트

# 그래프 입력 처리
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 인접 행렬로 처리
    graph[b][a] = 1

# BFS 함수
def bfs(x):  
    queue = deque()
    visited[x] = 1  # 시작 노드를 방문 처리
    queue.append(x)  # 시작 노드를 큐에 삽입
    
    while queue:
        a = queue.popleft()  # 큐에서 꺼낸 노드
        for i in range(1, n+1):  # 인접 노드 탐색
            if graph[a][i] == 1 and visited[i] == 0:  # 연결되어 있고 미방문 상태일 경우
                queue.append(i)
                visited[i] = visited[a] + 1  # 방문 처리 및 거리 기록

# 1번 노드에서 BFS 시작
bfs(1)

# 결과 계산
result = 0
for i in range(2, n+1):
    if visited[i] < 4 and visited[i] != 0:  # 거리 3 이하이고 방문된 노드
        result += 1

print(result)
