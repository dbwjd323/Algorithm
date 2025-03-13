function solution(n) {
    let result = [];
    let divisor = 2;
    
    while(n>1){
        if(n%divisor === 0){
        result.push(divisor);
        while(n%divisor === 0){
            n /= divisor;
        }
    }
        divisor++;
    }
    return result;
}