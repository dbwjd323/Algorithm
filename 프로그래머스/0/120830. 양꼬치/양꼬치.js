function solution(n, k) {
    if (n < 10){
        return n*12000 + k*2000;
    } else {
        let service = Math.floor(n/10);
        return n*12000 + k*2000 - service*2000;
    }
}