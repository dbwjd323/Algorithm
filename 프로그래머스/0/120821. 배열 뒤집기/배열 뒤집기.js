function solution(num_list) {    
    let stack = [];
    
    while(num_list.length > 0){
        let number = num_list.pop();
        stack.push(number);
    }
    
    return stack;
}