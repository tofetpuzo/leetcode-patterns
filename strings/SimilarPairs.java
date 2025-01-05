import java.util.*;

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

        // Map to store the frequency of each character signature
        Map<String, Integer> signatureFreq = new HashMap<>();
        
        // Convert each string to its signature and count frequencies
        for (String word : words) {
            String signature = getSignature(word);
            signatureFreq.merge(signature, 1, Integer::sum);
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
        char[] chars = word.toCharArray();
        Set<Character> uniqueChars = new TreeSet<>();
        for (char c : chars) {
            uniqueChars.add(c);
        }
        StringBuilder sb = new StringBuilder();
        for (char c : uniqueChars) {
            sb.append(c);
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
