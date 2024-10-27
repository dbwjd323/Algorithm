n = int(input())

stack = []
result = []
cur = 1 # 현재 스택에 넣을 수

for _ in range(n):
    num = int(input())
    # 현재 수(num)까지 stack에 push
    while cur <= num:
        stack.append(cur)
        result.append('+')
        cur += 1
        
    # 스택의 top이 현재 수와 일치하면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택의 top이 현재 수와 일치하지 않으면 "NO"
    else:
        result.clear() # 출력할 result 리스트 비우기
        result.append('NO')
        break
        
for answer in result:
    print(answer)
