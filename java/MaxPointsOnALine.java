import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;

public class MaxPointsOnALine {
    public int maxPoints(int[][] points) {
        if(points.length == 1) {
            return 1;
        }
        HashMap<ArrayList<Float>, HashSet<int[] > > history = new HashMap<ArrayList<Float>, HashSet<int[]>>();

        for(int i = 0; i < points.length - 1; i++) {
            for(int j = i + 1; j < points.length; j++) {
                int[] point1 = points[i];
                int[] point2 = points[j];
                ArrayList<Float> information = new ArrayList();
                if ((point1[0] - point2[0]) != 0) {
                    information.add((float)(point1[1] - point2[1]) / (float)(point1[0] - point2[0]));
                    information.add(information.get(0) * (float)-point1[0] + (float)point1[1]);
                } else {
                    information.add((float) 2 * 10000 + 1);
                    information.add((float)point1[0]);
                }

                HashSet<int[] > set = history.get(information);
                if (set == null) {
                    set = new HashSet<>();
                    history.put(information, set);
                }
                set.add(point1);
                set.add(point2);
            }
        }
        return history.values().stream().mapToInt(HashSet::size).max().getAsInt();

    }
}
