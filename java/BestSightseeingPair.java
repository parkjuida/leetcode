
public class BestSightseeingPair {
    public int maxScoreSightseeingPair(int [] values) {
        int [] answer = new int[values.length];
        answer[values.length - 1] = values[values.length - 1] + values[0] - values.length + 1;

        for(int i = values.length - 2; i > 0; i--) {
            answer[i] = Math.max(answer[i + 1], values[i] + values[0] - i);
        }

        int ret = answer[1];
        for(int i = 1; i < answer.length - 1; i++) {
            ret = Math.max(ret, answer[i + 1] - values[0] + values[i] + i);
        }

        return ret;
    }

    public static void main(String[] args) {
        BestSightseeingPair bestSightseeingPair = new BestSightseeingPair();
        int ret = bestSightseeingPair.maxScoreSightseeingPair(new int[]{8,1,5,2,6});
        System.out.println(ret);
        ret = bestSightseeingPair.maxScoreSightseeingPair(new int[]{1,2});
        System.out.println(ret);
    }
}
