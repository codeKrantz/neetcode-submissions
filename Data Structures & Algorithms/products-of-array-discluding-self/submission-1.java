class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];

        //Nested for loop to iterate every once per element
        for (int i = 0; i < n; i++){
            int prod = 1;
            for(int j = 0; j < n; j++){
                //skips over the current number as described
                if (i!=j){
                    prod *= nums[j];
                }
            }
            //adding element to the list
            res[i] = prod;
        }
        return res;
    }
}  
