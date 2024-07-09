def solution(progresses, speeds):
    answer = []
    complete_days = []  # 각 기능의 완료까지 걸리는 일수를 저장할 리스트
    
    # 각 기능의 완료까지 걸리는 일수 계산
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        days = (100 - progress) // speed  # 완료까지 걸리는 일수 계산
        if (100 - progress) % speed != 0:
            days += 1
        complete_days.append(days)
    
    # 배포될 기능 수 계산
    count = 1  # 첫 번째 기능은 무조건 배포 가능
    max_days = complete_days[0]
    
    for i in range(1, len(complete_days)):
        if complete_days[i] <= max_days:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_days = complete_days[i]
    
    # 마지막에 count가 남아있는 경우 추가
    answer.append(count)
    
    return answer