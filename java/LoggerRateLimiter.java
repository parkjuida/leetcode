import java.util.HashMap;

class Logger {
    HashMap<String, Integer> history;

    /** Initialize your data structure here. */
    public Logger() {
        history = new HashMap<>();
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
     If this method returns false, the message will not be printed.
     The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(history.containsKey(message)) {
            int savedTimeStamp = history.get(message);

            if(timestamp - savedTimeStamp < 10) {
                return false;
            } else {
                history.put(message, timestamp);
                return true;
            }

        } else {
            history.put(message, timestamp);
            return true;
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */