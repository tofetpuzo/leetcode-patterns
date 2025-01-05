import java.util.*;

public class SimilarPairs {
    public static long countSimilarPairs(List<String> words) {
        int n = words.size();
        long count = 0;
        
        // Convert each string to its character set representation
        List<Set<Character>> wordSets = new ArrayList<>();
        for (String word : words) {
            Set<Character> charSet = new HashSet<>();
            for (char c : word.toCharArray()) {
                charSet.add(c);
            }
            wordSets.add(charSet);
        }
        
        // Compare each pair
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (wordSets.get(i).equals(wordSets.get(j))) {
                    count++;
                }
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        // Test case 1
        List<String> test1 = Arrays.asList("xyz", "foo", "of");
        System.out.println("Test 1 Result: " + countSimilarPairs(test1)); // Expected: 1

        // Test case 2
        List<String> test2 = Arrays.asList("abaca", "cba", "abc");
        System.out.println("Test 2 Result: " + countSimilarPairs(test2)); // Expected: 3

        // Test case 3
        List<String> test3 = Arrays.asList("aaa", "bbb", "ccc");
        System.out.println("Test 3 Result: " + countSimilarPairs(test3)); // Expected: 0
    }
}
