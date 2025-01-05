public class AdRotation {
    /**
     * Rotates the advertisement display pattern by flipping all bits.
     * 1 becomes 0 (displayed becomes hidden) and vice versa.
     * 
     * @param currentDisplay the current display pattern as a base 10 number
     * @return the new display pattern as a base 10 number
     */
    public static int rotateAds(int currentDisplay) {
        // Find the number of bits needed to represent the number
        int numBits = Integer.SIZE - Integer.numberOfLeadingZeros(currentDisplay);
        if (numBits == 0) numBits = 1; // Handle case when input is 0
        
        // Create a mask with 1s for all positions that matter
        int mask = (1 << numBits) - 1;
        
        // XOR with mask to flip all bits
        return currentDisplay ^ mask;
    }

    public static void main(String[] args) {
        // Test cases
        int[] tests = {30, 0, 1, 15, 7};
        
        for (int test : tests) {
            int result = rotateAds(test);
            System.out.printf("Input: %d (binary: %s)%n", 
                test, Integer.toBinaryString(test));
            System.out.printf("Output: %d (binary: %s)%n%n", 
                result, Integer.toBinaryString(result));
        }
    }
}
