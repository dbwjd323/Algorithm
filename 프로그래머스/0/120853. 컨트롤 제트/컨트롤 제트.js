function solution(s) {
    let numbers = s.split(" ");
    let arr = [];
    let result = 0;
    
    for(num of numbers){
        if(num === "Z"){
            arr.pop();
        } else {
            arr.push(Number(num));
        }
    }
    for(i of arr){
        result += i;
    }
    return result;
}