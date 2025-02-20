function solution(s){
   let stack = [];
    
    for(let char of s){
        if(char === "("){
            stack.push(char);
        } else { // char === ")"
            if(stack.length === 0) return false; // 짝이 맞지 않음
            stack.pop(); // 짝을 맞춰 제거
        }
    }
    return stack.length === 0; // 스택이 비어 있으면 올바른 괄호
}