import java.util.HashSet;
import java.util.Objects;
import java.util.PriorityQueue;

public class KthSmallestElementInASortedMatrix {
    class Value implements Comparable<Value> {
        int value;
        int row;
        int col;


        public Value(int v, int r, int c) {
            value = v;
            row = r;
            col = c;
        }

        @Override
        public int compareTo(Value v) {
            return this.value >= v.value ? 1: - 1;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Value value1 = (Value) o;
            return value == value1.value &&
                    row == value1.row &&
                    col == value1.col;
        }

        @Override
        public int hashCode() {
            return Objects.hash(value, row, col);
        }
    }

    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Value> queue = new PriorityQueue<>();
        HashSet<Value> history = new HashSet<>();

        int counter = 0;
        queue.add(new Value(matrix[0][0], 0, 0));
        Value v = null;

        while(counter < k) {
            v = queue.poll();
            if(v.row + 1 < matrix.length) {
                Value newV = new Value(matrix[v.row + 1][v.col], v.row + 1, v.col);
                if(!history.contains(newV)) {
                    queue.add(newV);
                    history.add(newV);
                }
            }
            if(v.col + 1 < matrix.length) {
                Value newV = new Value(matrix[v.row][v.col + 1], v.row, v.col + 1);
                if(!history.contains(newV)) {
                    queue.add(newV);
                    history.add(newV);
                }
            }
            counter++;
        }
        return v.value;
    }

    public static void main(String[] args) {
        KthSmallestElementInASortedMatrix kthSmallestElementInASortedMatrix = new KthSmallestElementInASortedMatrix();
        int[][] input = new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};
        int ret;
//        int ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 8);
//        System.out.println(ret);
//
//        input = new int[][]{{-5}};
//        ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 1);
//        System.out.println(ret);
//
//        input = new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};
//        ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 7);
//        System.out.println(ret);
//
//        input = new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};
//        ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 6);
//        System.out.println(ret);
//
//        input = new int[][]{{-11, -9, -5}, {-10, 11, 13}, {12, 13, 15}};
//        ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 4);
//        System.out.println(ret);

        input = new int[][]{
                {1, 4, 7, 11, 15},
                {2, 5, 8, 12, 19},
                {3, 6, 9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30},
        };
        ret = kthSmallestElementInASortedMatrix.kthSmallest(input, 20);
        System.out.println(ret);
    }
}
