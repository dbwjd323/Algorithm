N = int(input()) # 피연산자 개수 입력
exp = list(input()) # 후위 표기식 저장
num = [int(input()) for i in range(N)] # 피연산자 숫자 값
stack = [] # 피연산자를 저장할 스택

for i in exp:
    if i.isalpha():
        stack.append(num[ord(i)-65]) # 알파벳에 대응되는 피연산자 값을 넣기 위해 ord() - 65 사용
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
            
print('%.2f' %stack[0])