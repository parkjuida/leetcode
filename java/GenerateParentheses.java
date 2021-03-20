import java.util.ArrayList;
import java.util.List;

public class GenerateParentheses {
    List<String> ret = new ArrayList<>();

    public void generate(int toSpend, int toClose, String s) {
        if(toSpend == 0 && toClose == 0) {
            ret.add(s);
        }
        if(toSpend != 0) {
            generate(toSpend - 1, toClose + 1, s + "(");
        }
        if(toClose != 0) {
            generate(toSpend, toClose - 1, s + ")");
        }

    }

    public List<String> generateParenthesis(int n) {
        generate(n, 0, "");
        return ret;
    }
}
