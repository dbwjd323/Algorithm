function solution(n) {
    let quotient = Math.floor(n/7);
    if(quotient <= 1){
        return 1;
    } else if (n%7 === 0){
        return quotient;
    } else {
        return quotient + 1;
    }
}