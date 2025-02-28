function solution(money) {
    let coffee = 5500;
    let cup = Math.floor(money / coffee);
    let extra = money % coffee;
    
    return [cup, extra];
}