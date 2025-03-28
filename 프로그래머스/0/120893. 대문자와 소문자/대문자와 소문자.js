function solution(my_string) {
    return my_string
        .split("")
        .map(char => char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase())
    .join("");
}