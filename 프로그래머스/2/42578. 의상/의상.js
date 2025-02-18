function solution(clothes) {
    let map = new Map();
    let answer = 1;
    
    for(let [cloth, type] of clothes){
        map.set(type, map.get(type)+1 || 1)
    }
    
    for(let[type, value] of map){
        answer *= (value+1);
    }
    return answer - 1;
}