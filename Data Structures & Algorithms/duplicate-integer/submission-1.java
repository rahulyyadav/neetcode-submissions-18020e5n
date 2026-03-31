class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        for (int i : nums) { 
            if (hashset.contains(i)) {
                return true;
            }
            hashset.add(i);
        }
        return false;
        
    }
}
