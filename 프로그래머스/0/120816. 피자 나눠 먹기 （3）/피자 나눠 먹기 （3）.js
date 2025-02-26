function solution(slice, n) {
    // n을 slice로 나눠서 나머지가 0이면 몫이 result가 된다
    // n을 slice로 나눠서 나머지가 1 이상이면 몫 + 1이 된다
    let modulus = n % slice
    if (modulus === 0){
        return n / slice;
    } else {
        return Math.floor(n / slice) + 1;
    }
}