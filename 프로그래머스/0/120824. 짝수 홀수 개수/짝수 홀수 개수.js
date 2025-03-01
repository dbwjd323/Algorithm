function solution(num_list) {
    let answer = [];
    let even =0, odd = 0;
    
    for (num of num_list){
        if (num % 2 === 0){
            even += 1;
        } else {
            odd += 1;
        }
    }
    answer.push(even, odd);
    return answer;
}