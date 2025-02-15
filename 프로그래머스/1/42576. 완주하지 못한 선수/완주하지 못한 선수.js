function solution(participant, completion) {
    let map = new Map();
    
    for(let person of participant){
        map.set(person, (map.get(person) || 0) + 1);
    }
    
    for(let person of completion){
        map.set(person, map.get(person) - 1 );
    }
    
    for (let [person, count] of map){
        if(count > 0){
            return person;
        }
    }
}