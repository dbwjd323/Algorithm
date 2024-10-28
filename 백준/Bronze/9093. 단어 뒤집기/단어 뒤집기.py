n = int(input())

for _ in range(n):
    string = input().split()
    for word in string:
        print(word[::-1], end=' ')