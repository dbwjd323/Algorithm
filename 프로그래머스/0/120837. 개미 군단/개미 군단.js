function solution(hp) {
    let count = 0;
    
    if(hp/5) {
        count = Math.floor(hp/5) + Math.floor(hp%5/3) + Math.floor(hp%5%3/1);
    } else if(hp/3) {
        count = Math.floor(hp/3) + Math.floor(hp%3/1);
    } else {
        count = hp;
    }
    
    return count;
}