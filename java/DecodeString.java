class DecodeString {
    class Pair {
        String str;
        int index;

        Pair(String str, int index) {
            this.str = str;
            this.index = index;
        }
    }

    public Pair decode(char[] s, int index) {
        if(index > s.length) {
            return new Pair("", s.length);
        }
        StringBuilder currentString = new StringBuilder();
        StringBuilder currentNumber = new StringBuilder();
        int currentIndex = index;
        while(currentIndex < s.length) {
            while (currentIndex < s.length && s[currentIndex] != '[' && s[currentIndex] != ']') {
                if (s[currentIndex] >= 'a' && s[currentIndex] <= 'z') {
                    currentString.append(s[currentIndex]);
                }
                if (s[currentIndex] >= '0' && s[currentIndex] <= '9') {
                    currentNumber.append(s[currentIndex]);
                }
                currentIndex++;
            }
            if (currentIndex < s.length && s[currentIndex] == ']') {
                return new Pair(currentString.toString(), currentIndex + 1);
            }
            int iterNumber = 0;
            if (currentNumber.length() != 0) {
                iterNumber = Integer.parseInt(currentNumber.toString());
                currentNumber = new StringBuilder();
            }
            Pair pair = decode(s, currentIndex + 1);
            for (int i = 0; i < iterNumber; i++) {
                currentString.append(pair.str);
            }
            currentIndex = pair.index;
        }

        return new Pair(currentString.toString(), currentIndex - index + 1);
    }

    public String decodeString(String s) {
        return decode(s.toCharArray(), 0).str;
    }
}