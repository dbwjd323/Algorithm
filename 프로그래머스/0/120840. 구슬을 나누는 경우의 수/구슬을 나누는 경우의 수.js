function solution(balls, share) {
    let up = 1;
    let down = 1;
    for(let i = balls; i>balls - share; i--){
        up *= i;
        
    }
    for(let i = share; i>0; i--){
        down *= i;
    }
    return up/down;
}