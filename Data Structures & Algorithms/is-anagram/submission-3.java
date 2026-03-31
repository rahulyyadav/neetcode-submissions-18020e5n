class Solution {
    public boolean isAnagram(String s, String t) {
        
        Map<Character, Integer> CountS = new HashMap<>();
        Map<Character, Integer> CountT = new HashMap<>();

        if(s.length() != t.length()){
            return false;
        }

        // count frequencies of s and t. 
        
        for(int i = 0; i < s.length(); i++){

            char charS = s.charAt(i);
            char charT = t.charAt(i);

            // update count for s and t.
            CountS.put(charS, CountS.getOrDefault(charS, 0) + 1);
            CountT.put(charT, CountT.getOrDefault(charT, 0) + 1);
        }


        // Compare character frequencies

        for(char c: CountS.keySet()){
            if(CountS.get(c).intValue() != CountT.getOrDefault(c, 0)){
                return false;
            }
        }
        return true;
    }
}
