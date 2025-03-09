function solution(n) {
    let count = 0;
    
    for (let i = 4; i<=n; i++){
        let divisorcount = 0;
        
        for (let j = 1; j <= i; j++){
            if (i%j === 0) divisorcount++;
        }
        if(divisorcount > 2) count++;
    }
    return count;
}