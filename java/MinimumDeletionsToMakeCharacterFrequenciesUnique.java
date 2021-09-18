import java.util.HashMap;
import java.util.HashSet;

public class MinimumDeletionsToMakeCharacterFrequenciesUnique {
    public int minDeletions(String s) {
        HashMap<Character, Integer> history = new HashMap<>();

        for(char c: s.toCharArray()) {
            history.put(c, history.getOrDefault(c, 0) + 1);
        }
        HashSet<Integer> counter = new HashSet<>();
        int answer = 0;
        for(char c: history.keySet()) {
            int number = history.get(c);
            if(counter.contains(history.get(c))) {
                while (number > 0 && counter.contains(number)) {
                    number--;
                    answer++;
                }
                if(number > 0) {
                    counter.add(number);
                }
            } else {
                counter.add(history.get(c));
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        MinimumDeletionsToMakeCharacterFrequenciesUnique mdtmcf = new MinimumDeletionsToMakeCharacterFrequenciesUnique();
        int ret;
        ret = mdtmcf.minDeletions("aab");
        System.out.println(ret);
        ret = mdtmcf.minDeletions("aaabbbcc");
        System.out.println(ret);
        ret = mdtmcf.minDeletions("ceabaacb");
        System.out.println(ret);
        ret = mdtmcf.minDeletions("aaaabbbbcccdde");
        System.out.println(ret);
    }

}
