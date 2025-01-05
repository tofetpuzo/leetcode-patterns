import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SimilarPairs {
    /**
     * Counts the number of similar string pairs in the given list.
     * Two strings are similar if they contain exactly the same set of characters.
     * Time Complexity: O(n * k * log k) where n is number of strings and k is average string length
     * Space Complexity: O(n)
     *
     * @param words List of strings to compare
     * @return Number of similar pairs
     * @throws IllegalArgumentException if input list is null
     */
    public static long countSimilarPairs(List<String> words) {
        if (words == null) {
            throw new IllegalArgumentException("Input list cannot be null");
        }

        if (words.isEmpty()) {
            return 0;
        }

        // Map to store the frequency of each character signature
        Map<String, Integer> signatureFreq = new HashMap<>();
        
        // Convert each string to its signature and count frequencies
        for (String word : words) {
            String signature = getSignature(word);
            signatureFreq.merge(signature, 1, (a, b) -> a + b);
        }
        
        // Calculate pairs using combination formula: n*(n-1)/2
        long count = 0;
        for (int freq : signatureFreq.values()) {
            if (freq > 1) {
                count += (long) freq * (freq - 1) / 2;
            }
        }
        
        return count;
    }
    
    /**
     * Converts a string to its character signature (sorted unique characters)
     * @param word Input string
     * @return Signature string
     */
    private static String getSignature(String word) {
        if (word == null || word.isEmpty()) {
            return "";
        }
        
        // Create boolean array for all possible characters
        boolean[] present = new boolean[128];
        
        // Mark presence of each character
        for (char c : word.toCharArray()) {
            present[c] = true;
        }
        
        // Build signature string
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 128; i++) {
            if (present[i]) {
                sb.append((char)i);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        try {
            // Test case 1
            List<String> test1 = Arrays.asList("xyz", "foo", "of");
            System.out.println("Test 1 Result: " + countSimilarPairs(test1)); // Expected: 1

            // Test case 2
            List<String> test2 = Arrays.asList("abaca", "cba", "abc");
            System.out.println("Test 2 Result: " + countSimilarPairs(test2)); // Expected: 3

            // Test case 3
            List<String> test3 = Arrays.asList("aaa", "bbb", "ccc");
            System.out.println("Test 3 Result: " + countSimilarPairs(test3)); // Expected: 0

            // Additional test case with null
            System.out.println("Test null input: " + countSimilarPairs(null));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
