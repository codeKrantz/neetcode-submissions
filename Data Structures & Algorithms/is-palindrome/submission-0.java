class Solution {
    public boolean isPalindrome(String s) {
        String text = s.replaceAll("[\\s\\W]", "").toLowerCase();
        for(int i = 0; i < (text.length()/2); i++){
            char c = text.charAt(i);
            int place = text.length() - i - 1;
            char z = text.charAt(place);
            if(c!=z){
                return false;
            }
        }
        return true;
    }
}
