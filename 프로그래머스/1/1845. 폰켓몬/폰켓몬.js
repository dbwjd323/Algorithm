function solution(nums) {
    // 먼저 nums의 길이를 알고 nums/2 값을 알아낸다.
    const ans = nums.length / 2;
    // nums를 정렬
    nums.sort();
    
    // nums의 중복을 제거하기 위해 set() 사용.
    const set = new Set(nums);
    
    if(ans >= set.size){
        return set.size;
    } else {
        return ans;
    }
}