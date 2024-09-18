T = int(input()) #테스트 케이스 개수

for _ in range(T):
    k = int(input()) #1층
    n = int(input()) #3호
    #0층 리스트
    f0 = [x for x in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            f0[j] += f0[j-1] 
    print(f0[-1])
            
        

