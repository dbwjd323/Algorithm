N = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while N != answer:
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            N[i], N[i+1] = N[i+1], N[i]
            print(" ".join(map(str, N)))
