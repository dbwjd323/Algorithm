function solution(progresses, speeds) {
    let days = progresses.map((progress, i) => Math.ceil((100 - progress) / speeds[i]));
    let queue = [];
    let maxDay = days[0];  // 첫 번째 작업의 완료 예상 날짜
    let count = 0;

    for (let day of days) {
        if (day <= maxDay) {
            count++; // 같은 배포 그룹
        } else {
            queue.push(count); // 이전 배포 그룹 저장
            count = 1; // 새로운 배포 그룹 시작
            maxDay = day; // 새로운 기준 업데이트
        }
    }

    queue.push(count); // 마지막 배포 그룹 추가

    return queue;
}
