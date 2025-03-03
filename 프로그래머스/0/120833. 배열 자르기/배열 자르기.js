function solution(numbers, num1, num2) {
    let answer = [];
    for(let i = 0; i <= num2; i++){
        if (i >= num1){
            answer.push(numbers[i]);
        }
    }
    return answer;
}