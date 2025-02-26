function solution(n) {
    // n과 6의 최소공배수를 구한 후 -> 6으로 나눈 몫
    answer = n * 6 / GCD(n, 6);
    return answer / 6;
}

function GCD(a, b){
    return b === 0 ? a : GCD(b, a % b);
}