function solution(bridge_length, weight, truck_weights) {
    let time = 0; // 경과 시간
    let onBridge = Array(bridge_length).fill(0); // 다리 위 상태 (초기에는 빈 다리)
    let sum = 0; // 다리 위 트럭 무게 총합

    while (truck_weights.length > 0 || sum > 0) {
        time++; // 시간 증가

        // 다리에서 가장 앞에 있는 트럭 제거
        sum -= onBridge.shift(); 

        // 새로운 트럭이 다리에 올라갈 수 있는지 확인
        if (truck_weights.length > 0 && sum + truck_weights[0] <= weight) {
            let truck = truck_weights.shift();
            onBridge.push(truck);
            sum += truck;
        } else {
            onBridge.push(0); // 트럭이 못 올라가면 0 추가 (다리 유지)
        }
    }

    return time;
}
