function solution(emergency) {
    //원래 인덱스 위치 기억
    let indexed = emergency.map((num, idx) => [num, idx])
    // 내림차순
    indexed.sort((a, b) => b[0] - a[0]);
    
    let result = new Array(emergency.length);
    // 정렬된 순서대로 등수 
    indexed.forEach(([num, idx], rank) => {
        result[idx] = rank + 1;
    });
    
    return result;
}