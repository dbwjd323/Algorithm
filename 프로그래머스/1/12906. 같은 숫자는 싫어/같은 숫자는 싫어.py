def solution(arr):
    answer = []
    now = arr[0]
    answer.append(now)
    for i in arr:
        if now != i:
            answer.append(i)
            now = i
    return answer