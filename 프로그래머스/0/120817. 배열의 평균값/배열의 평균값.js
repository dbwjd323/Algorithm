function solution(numbers) {
    let sum = 0;
    
    for(n of numbers){
        sum += n;
    }
    let answer = sum / numbers.length;
    return answer;
}