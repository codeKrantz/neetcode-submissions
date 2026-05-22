class Solution {
    public int[] twoSum(int[] nums, int target) {
        //brute force
        for(int i = 0; i < nums.length; i++){
            for (int c = i+1; c < nums.length; c++){
                if(nums[i] + nums[c] == target){
                    int first = i;
                    int next = c;
                    return new int[]{first, next};
                }
                else{
                    continue;
                }
            }
        }
        return new int[]{};
    }
}
