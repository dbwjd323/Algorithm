S = input()
stack = []
result = ''
is_tag = False  # 태그 안에 있는지 확인하는 용도

for i in S:
    if i == '<':
        # 태그 시작, 이전에 쌓인 단어 뒤집어서 추가
        while stack:
            result += stack.pop()
        is_tag = True  # 태그 모드 진입
        result += i  # '<'는 그대로 추가
    elif i == '>':
        # 태그 종료
        is_tag = False  # 태그 모드 종료
        result += i  # '>'는 그대로 추가
    elif is_tag:
        # 태그 내부 문자
        result += i  # 태그 안의 내용은 뒤집지 않고 그대로 추가
    elif i == ' ': # 태그 밖의 공백
        # 공백을 만나면 단어 뒤집어서 추가
        while stack:
            result += stack.pop()
        result += ' '  # 공백 추가
    else: # 태그 밖의 문자
        stack.append(i)  # 스택에 문자 추가 (뒤집기 위해)

# 마지막 단어 처리 - 문자열의 끝에 도달했을 때 스택에 남아 있는 단어를 뒤집어서 결과에 추가
while stack: 
    result += stack.pop()

print(result)
