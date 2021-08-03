import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

class Trie {
    private HashMap<Character, HashMap> tree;
    /** Initialize your data structure here. */
    public Trie() {
        tree = new HashMap<>();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        HashMap<Character, HashMap> tempTree = this.tree;
        for(char w: word.toCharArray()) {
            if(!tempTree.containsKey(w)) {
                tempTree.put(w, new HashMap<Character, HashMap>());
            }
            tempTree = tempTree.get(w);
        }
        tempTree.put('$', null);
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        HashMap<Character, HashMap> tempTree = this.tree;
        for(char w: word.toCharArray()) {
            if(!tempTree.containsKey(w)) {
                return false;
            }
            tempTree = tempTree.get(w);
        }
        if(tempTree.containsKey('$')) {
            return true;
        }
        return false;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        HashMap<Character, HashMap> tempTree = this.tree;
        for(char w: prefix.toCharArray()) {
            if(!tempTree.containsKey(w)) {
                return false;
            }
            tempTree = tempTree.get(w);
        }
        return true;
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("apple");
        System.out.println(trie.search("apple"));
        System.out.println(trie.search("app"));
        System.out.println(trie.startsWith("app"));
        trie.insert("app");
        System.out.println(trie.search("app"));
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */