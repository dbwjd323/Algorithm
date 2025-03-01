function solution(my_string, n) {
    let str = my_string.split("");
    let answer = "";
    
    for (s of str){
        answer += s.repeat(n);
    }
    
    return answer;
}