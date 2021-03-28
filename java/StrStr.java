public class StrStr {
    public int strStr(String haystack, String needle) {
        int needleIndex = 0;
        if(needle.length() == 0) {
            return 0;
        }
        for(int i = 0; i < haystack.length(); i++) {
            if (haystack.toCharArray()[i] == needle.charAt(needleIndex)) {
                needleIndex++;
                if(needleIndex == needle.length()) {
                    return i - needleIndex + 1;
                }
            } else {
                i = i - needleIndex;
                needleIndex = 0;
            }
        }
        return -1;
    }
}
