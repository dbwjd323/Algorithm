function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;
    
    sizes.forEach(([w, h]) => {
        const [big, small] = w>h ? [w,h] : [h, w];
        maxWidth = Math.max(maxWidth, big);
        maxHeight = Math.max(maxHeight, small);
    })
     
    return maxWidth * maxHeight;
}