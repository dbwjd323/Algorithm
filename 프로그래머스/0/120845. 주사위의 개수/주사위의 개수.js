function solution(box, n) {
    let width = box[0];
    let length = box[1];
    let height = box[2];
    
    return Math.floor(width/n) * Math.floor(length/n) * Math.floor(height/n);
}