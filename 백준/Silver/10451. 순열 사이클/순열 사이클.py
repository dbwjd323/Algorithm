T = int(input())

def check_cycle(node):
    visited[node]=True
    next_node = arr[node]
    if not visited[next_node]:
        check_cycle(next_node)
        
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False for _ in range(N+1)]
    circle = 0
    for i in range(1, N+1):
        if not visited[i]:
            circle += 1
            check_cycle(i)
    print(circle)