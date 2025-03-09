function solution(numbers, direction) {
    if (direction === "right"){
        let num = numbers.pop();
        numbers.unshift(num);
    } else {
        let num = numbers.shift();
        numbers.push(num);
    }
    return numbers;
}