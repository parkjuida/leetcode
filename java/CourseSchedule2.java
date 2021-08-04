import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;


public class CourseSchedule2 {
    public ArrayList<Integer> isOk(int course, HashMap<Integer, ArrayList<Integer>> curriculum, boolean[] visited, HashSet<Integer> history) {
        ArrayList<Integer> sequence = new ArrayList<>();
        if(history.contains(course)) {
            return null;
        }
        if(visited[course]) {
            return sequence;
        }

        if(!curriculum.containsKey(course)) {
            visited[course] = true;
            sequence.add(course);
            return sequence;
        }
        ArrayList<Integer> prerequisitesOfCourse = curriculum.get(course);
        history.add(course);

        for(Integer prerequisite: prerequisitesOfCourse) {
            ArrayList<Integer> ret = isOk(prerequisite, curriculum, visited, (HashSet<Integer>) history.clone());
            if(ret == null) {
                return null;
            }
            sequence.addAll(ret);
            visited[course] = true;
        }
        sequence.add(course);
        return sequence;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        HashMap<Integer, ArrayList<Integer>> curriculum = new HashMap<>();
        ArrayList<Integer> pre;
        for(int[] prerequisite:prerequisites) {
            if(!curriculum.containsKey(prerequisite[0])) {
                pre = new ArrayList<>();
                pre.add(prerequisite[1]);
                curriculum.put(prerequisite[0], pre);
            } else {
                pre = curriculum.get(prerequisite[0]);
                pre.add(prerequisite[1]);
                curriculum.put(prerequisite[0], pre);
            }
        }

        boolean[] visited = new boolean[numCourses];
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            if(visited[i]) {
                continue;
            }
            pre = isOk(i, curriculum, visited, new HashSet<Integer>());

            if(pre == null) {
                return new int[]{};
            }
            answer.addAll(pre);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        CourseSchedule2 cs = new CourseSchedule2();
        int[] result = cs.findOrder(2, new int[][]{{1, 0}});
//        Arrays.stream(result).forEach(System.out::println);
//        result = cs.findOrder(4, new int[][]{{1, 0}, {2, 0}, {3, 1}, {3, 2}});
//        Arrays.stream(result).forEach(System.out::println);
//        result = cs.findOrder(1, new int[][]{});
//        Arrays.stream(result).forEach(System.out::println);

//        result = cs.findOrder(1, new int[][]{{0, 0}});
//        Arrays.stream(result).forEach(System.out::println);
//        result = cs.findOrder(3, new int[][]{{1, 0}});
//        Arrays.stream(result).forEach(System.out::println);

//        result = cs.findOrder(4, new int[][]{{2, 0},{1, 0}, {3, 1}, {3, 2}, {1, 3}});
//        Arrays.stream(result).forEach(System.out::println);
//        result = cs.findOrder(3, new int[][]{{0, 1},{0, 2}, {1, 2}});
//        Arrays.stream(result).forEach(System.out::println);
        result = cs.findOrder(7, new int[][]{{1, 0},
                {0, 3}, {0, 2}, {3, 2}, {2, 5}, {4, 5}, {5,6}, {2, 4}});
        Arrays.stream(result).forEach(System.out::println);
    }
}
