import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;

public class FourSum2 {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        HashMap<Integer, Integer> mergedNums1 = new HashMap<>();

        initHashMaps(nums1, nums2, mergedNums1, 1);

        int answer = 0;
        for(int i = 0; i < nums3.length; i++) {
            for(int j = 0; j < nums4.length; j++) {
                answer += mergedNums1.getOrDefault(-(nums3[i] + nums4[j]), 0);
            }
        }

        return answer;
    }

    private void initHashMaps(int[] nums1, int[] nums2, HashMap<Integer, Integer> mergedNums1, int minus) {
        for(int i = 0; i < nums1.length; i++) {
            for(int j = 0; j < nums2.length; j++) {
                int key = (nums1[i] + nums2[j]) * minus;
                int value = mergedNums1.getOrDefault(key, 0);
                mergedNums1.put(key, value + 1);
            }
        }
    }

    public static void main(String[] args) {
        FourSum2 fourSum2 = new FourSum2();
        int result;
        result = fourSum2.fourSumCount(
                new int[]{1, 2},
                new int[]{-2, -1},
                new int[]{-1, 2},
                new int[]{0, 2}
        );
        System.out.println(result);
        result = fourSum2.fourSumCount(
                new int[]{0,},
                new int[]{-1},
                new int[]{1},
                new int[]{0,}
        );
        System.out.println(result);
        result = fourSum2.fourSumCount(
                new int[]{-1,1,1,1,-1},
                new int[]{0,-1,-1,0,1},
                new int[]{-1,-1,1,-1,-1},
                new int[]{0,1,0,-1,-1}
                );
        System.out.println(result);
    }
}
