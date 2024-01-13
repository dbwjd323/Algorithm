def solution(array):
    # 빈도수를 저장할 딕셔너리 초기화
    counts = {}

    # 배열의 각 원소의 빈도수 세기
    for num in array:
        counts[num] = counts.get(num, 0) + 1

    # 최빈값 찾기
    max_count = max(counts.values())
    mode_candidates = [key for key, value in counts.items() if value == max_count]

    # 최빈값이 여러 개인 경우 -1 반환
    if len(mode_candidates) > 1:
        return -1
    
    # 최빈값 반환
    return mode_candidates[0]