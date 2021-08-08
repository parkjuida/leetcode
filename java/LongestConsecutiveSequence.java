import java.util.HashMap;
import java.util.HashSet;

public class LongestConsecutiveSequence {
    public int getConsecutiveElement(int num, HashMap<Integer, Integer> numberMap) {
        if(!numberMap.containsKey(num)) {
            return 0;
        }
        if(numberMap.get(num) > 0) {
            return numberMap.get(num);
        }
        int value = 1 + getConsecutiveElement(num + 1, numberMap);
        numberMap.put(num, value);
        return value;
    }

    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> numberMap = new HashMap<>();
        for(int num: nums) {
            numberMap.put(num, 0);
        }
        int answer = 0;
        for(int num: numberMap.keySet()) {
            answer = Math.max(answer, getConsecutiveElement(num, numberMap));
        }

        return answer;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequence longestConsecutiveSequence = new LongestConsecutiveSequence();
        int result;
        result = longestConsecutiveSequence.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2});
        System.out.println(result);
        result = longestConsecutiveSequence.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1});
        System.out.println(result);
        result = longestConsecutiveSequence.longestConsecutive(new int[]{});
        System.out.println(result);
        result = longestConsecutiveSequence.longestConsecutive(new int[]{0});
        System.out.println(result);
        result = longestConsecutiveSequence.longestConsecutive(new int[]{0, 1});
        System.out.println(result);
        result = longestConsecutiveSequence.longestConsecutive(new int[]{0, 100});
        System.out.println(result);

    }
}
