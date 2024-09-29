n, k = map(int, input().split())

index = 0
arr = list(range(1, n+1))
result = []

while len(arr) != 0:
    index += (k-1)
    index = index % len(arr)
    result.append(arr.pop(index))
    
print("<", end="")
for i in range(n-1):
    print(result[i], end=", ")
print(result[n-1], end = "")
print(">", end="")