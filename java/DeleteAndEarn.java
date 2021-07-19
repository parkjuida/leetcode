import java.util.*;
import java.util.stream.Collectors;


public class DeleteAndEarn {
    public int deleteAndEarn(int [] nums) {
        Map<Integer, Integer> numberCount = new HashMap<>();

        for(int num: nums) {
            int count = numberCount.getOrDefault(num, 0);
            numberCount.put(num, num + count);
        }

        List<Integer> keys = numberCount.keySet().stream().sorted(Integer::compareTo).collect(Collectors.toList());
        int prevPrevValue = 0, prevValue = 0, value = 0;
        int prevKey = -1;

        for(int key: keys) {
            value = numberCount.get(key);
            if(prevKey != -1) {
                if (key - prevKey == 1) {
                    value = Math.max(prevPrevValue + value, prevValue);
                } else {
                    value = value + prevValue;
                }
            }
            prevPrevValue = prevValue;
            prevValue = value;
            prevKey = key;
        }

        return value;
    }

    public static void main(String[] args) {
        DeleteAndEarn deleteAndEarn = new DeleteAndEarn();
        int result = deleteAndEarn.deleteAndEarn(new int[]{3, 4, 2});
        System.out.println(result);
    }
}
