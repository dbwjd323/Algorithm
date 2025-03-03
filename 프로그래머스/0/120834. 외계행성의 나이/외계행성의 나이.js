function solution(age) {
    let ageArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
    return age.toString().split("").map(num => ageArr[num]).join("");
}