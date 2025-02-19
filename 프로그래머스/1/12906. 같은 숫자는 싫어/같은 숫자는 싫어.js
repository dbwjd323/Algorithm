function solution(arr)
{
    const stack = [];
    
    for (let i of arr){
        if(stack.length === 0 || stack[stack.length - 1] !== i){
            stack.push(i);
        }
    }
    
    return stack;
}