function solution(my_string, letter) {
    let answer = "";
    for (str of my_string){
        if(str === letter){
            continue;
        } else {
            answer += str;
        }
    }
    return answer;
}