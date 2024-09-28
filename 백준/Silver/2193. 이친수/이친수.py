n = int(input())

dp = [0]*(n+1)
dp[1] = 1 # 1자리 이친수는 1개다

for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[n])