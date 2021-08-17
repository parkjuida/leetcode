import java.util.HashMap;

public class SubarraysWithKDifferentIntegers {
    public int subarraysWithKDistinct(int[] nums, int k) {
        int left = 0, right = 0;
        HashMap<Integer, Integer> numberOfNumbers = new HashMap<>();

        while (right < nums.length && numberOfNumbers.keySet().size() < k) {
            numberOfNumbers.put(nums[right], numberOfNumbers.getOrDefault(nums[right], 0) + 1);
            right++;
        }

        int answer = 0;
        while(right < nums.length) {
            if(numberOfNumbers.keySet().size() < k) {
                numberOfNumbers.put(nums[right], numberOfNumbers.getOrDefault(nums[right], 0) + 1);
                answer++;
                right++;
                continue;
            }
            if(numberOfNumbers.containsKey(nums[right])) {
                HashMap<Integer, Integer> tempNumberOfNumbers = new HashMap<>();
                for(int i = left; i <= right - k; i++) {
                    tempNumberOfNumbers.put(nums[i], tempNumberOfNumbers.getOrDefault(nums[i], 0) + 1);
                    answer++;
                    if(numberOfNumbers.get(nums[i]) - tempNumberOfNumbers.get(nums[i]) == 0) {
                        break;
                    }
                }
                numberOfNumbers.put(nums[right], numberOfNumbers.get(nums[right]) + 1);
                right++;
                continue;
            }

            while (left < right && numberOfNumbers.keySet().size() >= k) {
                int leftValue = numberOfNumbers.get(nums[left]);

                if(leftValue == 1) {
                    numberOfNumbers.remove(nums[left]);
                    left++;
                    break;
                } else {
                    numberOfNumbers.put(nums[left], leftValue - 1);
                }
                answer++;
                left++;
            }
        }

        while (right - left >= k && numberOfNumbers.keySet().size() >= k) {
            int leftValue = numberOfNumbers.get(nums[left]);
            answer++;
            if(leftValue == 1) {
                numberOfNumbers.remove(nums[left]);
                break;
            } else {
                numberOfNumbers.put(nums[left], leftValue - 1);
            }
            left++;
        }

        return answer;
    }

    public static void main(String[] args) {
        SubarraysWithKDifferentIntegers subarray = new SubarraysWithKDifferentIntegers();
        int[] nums = new int[]{1, 2, 3, 1, 2, 3};
//        System.out.println(subarray.subarraysWithKDistinct(nums, 2));
//        nums = new int[]{1, 2, 1, 2, 1,2,1,2,3};
//        System.out.println(subarray.subarraysWithKDistinct(nums, 3));
//        nums = new int[]{2,1,2,1,1};
//        System.out.println(subarray.subarraysWithKDistinct(nums, 3));
        nums = new int[]{2,2,1,1,1,2,1,1,1};
        System.out.println(subarray.subarraysWithKDistinct(nums, 2));

    }
}
