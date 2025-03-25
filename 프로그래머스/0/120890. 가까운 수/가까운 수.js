function solution(array, n) {
    let answer = array[0]; //초기값 설정
    
    for (num of array){
        let diffA = Math.abs(answer - n);
        let diffB = Math.abs(num - n);
        
        if(diffB < diffA || (diffA===diffB && num < answer)){
            answer = num;
        }
    }
    return answer;
}