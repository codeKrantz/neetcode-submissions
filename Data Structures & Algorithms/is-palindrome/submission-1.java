class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[\\s\\W]", "").toLowerCase();
        for(int i = 0; i < (s.length()/2); i++){
            char c = s.charAt(i);
            int place = s.length() - i - 1;
            char z = s.charAt(place);
            if(c!=z){
                return false;
            }
        }
        return true;
    }
}
