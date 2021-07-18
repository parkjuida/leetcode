import java.util.*;

public class WordLadder {
    public boolean diffOneWord(String a, String b) {
        int counter = 0;
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) != b.charAt(i)) {
                counter++;
            }
        }
        if(counter == 1) {
            return true;
        }
        return false;
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Map<String, List<String>> transformMap = new HashMap<>();
        Map<String, Boolean> history = new HashMap<>();
        List<String> value;

        for (String key: wordList) {
            value = new ArrayList<>();
            for (String word: wordList) {
                if(diffOneWord(key, word)) {
                    value.add(word);
                }
            }
            transformMap.put(key, value);
            history.put(key, Boolean.FALSE);
        }

        Queue<Map<String, Integer>> queue = new LinkedList<>();
        Map<String, Integer> tempState;

        for (String key:wordList) {
            if(diffOneWord(key, beginWord)) {
                tempState = new HashMap<>();
                tempState.put(key, 2);
                queue.add(tempState);
            }
        }

        String currentString;
        int currentValue;
        while (!queue.isEmpty()) {
            tempState = queue.poll();
            currentString = (String) tempState.keySet().toArray()[0];

            if(history.get(currentString)) {
                continue;
            }

            history.put(currentString, Boolean.TRUE);
            currentValue = tempState.get(currentString);

            if(currentString.equals(endWord)) {
                return currentValue;
            }

            if (currentValue < wordList.size()) {
                List<String> nextWords = transformMap.get(currentString);
                Map<String, Integer> nextState;
                for(String word: nextWords) {
                    if(history.get(word)) {
                        continue;
                    }
                    nextState = new HashMap<>();
                    nextState.put(word, currentValue + 1);
                    queue.add(nextState);
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        WordLadder wordLadder = new WordLadder();
        List<String> list = new ArrayList<>();
        list.add("hot");
        list.add("cog");
        list.add("dog");
        list.add("tot");
        list.add("hog");
        list.add("hop");
        list.add("pot");
        list.add("dot");
        System.out.println(wordLadder.ladderLength("hot", "dog", list));
    }
}
