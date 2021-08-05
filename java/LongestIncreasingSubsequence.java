import java.util.Arrays;
import java.util.Stack;

public class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        int[] answers = new int[nums.length];
        Arrays.fill(answers, 1);
        int answer = 1;
        for(int i = 1; i < answers.length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    answers[i] = Math.max(answers[i], answers[j] + 1);
                }
            }
            answer = Math.max(answer, answers[i]);
        }
        return answer;
    }

    public static void main(String[] args) {
        LongestIncreasingSubsequence longestIncreasingSubsequence = new LongestIncreasingSubsequence();
        System.out.println(longestIncreasingSubsequence.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 17}));
        System.out.println(longestIncreasingSubsequence.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}));
        System.out.println(longestIncreasingSubsequence.lengthOfLIS(new int[]{7, 7, 7, 7, 7, 7, 7}));
        System.out.println(longestIncreasingSubsequence.lengthOfLIS(new int[]{7, 2, 1, 4, 1, 2, 4}));
    }
}
