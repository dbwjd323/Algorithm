function solution(rsp) {
    let rsprsp = rsp.split("");
    let answer = "";
    
    for (i of rsprsp) {
        if (i === '2'){
            answer += '0';
        } else if(i === '0') {
            answer += '5';
        } else {
            answer += '2';
        }
    }
    return answer;
}