public class ProcessParent {
    /**
     * Finds the parent process number for a given process in a process tree.
     * Process 1 spawns 1 child, process 2 spawns 2 children, and so on.
     * 
     * @param process the process number to find the parent for
     * @return the parent process number, or -1 if process is 1 (root)
     * @throws IllegalArgumentException if process number is invalid
     */
    public static int findParent(int process) {
        if (process < 1) {
            throw new IllegalArgumentException("Process number must be positive");
        }
        if (process == 1) {
            return -1; // Root process has no parent
        }

        int currentParent = 1;
        int nextProcessStart = 2;
        
        while (nextProcessStart <= process) {
            int childCount = currentParent;
            int rangeEnd = nextProcessStart + childCount - 1;
            
            if (process <= rangeEnd) {
                return currentParent;
            }
            
            currentParent++;
            nextProcessStart = rangeEnd + 1;
        }
        
        throw new IllegalArgumentException("Invalid process number: " + process);
    }

    public static void main(String[] args) {
        // Test cases
        int[] testProcesses = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        
        for (int process : testProcesses) {
            try {
                int parent = findParent(process);
                System.out.printf("Process %d's parent: %d%n", 
                    process, parent);
            } catch (IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
}
