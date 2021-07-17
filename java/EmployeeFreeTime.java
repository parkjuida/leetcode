import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class EmployeeFreeTime {
    public boolean canMerge(Interval a, Interval b) {
        return a.end >= b.start;
    }

    public Interval merge(Interval a, Interval b) {
        return new Interval(a.start, Math.max(a.end, b.end));
    }

    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> answer = new ArrayList<>();
        schedule.stream().flatMap(List::stream).sorted((a, b) -> {
            if (a.start <= b.start) {
                return -1;
            } else {
                return 1;
            }
        }).reduce((a, b) -> {
            if(canMerge(a, b)) {
                return merge(a, b);
            } else {
                answer.add(new Interval(a.end, b.start));
                return b;
            }
        });

        return answer;
    }

    public static void main(String[] args) {
        List<List<Interval>> intervals = new ArrayList<>();
        ArrayList<Interval> interval = new ArrayList<Interval>();
        interval.add(new Interval(1, 3));
        intervals.add((List<Interval>)interval.clone());
        interval.clear();

        interval.add(new Interval(6, 7));
        intervals.add((List<Interval>)interval.clone());
        interval.clear();

        interval.add(new Interval(2, 4));
        intervals.add((List<Interval>)interval.clone());
        interval.clear();

        interval.add(new Interval(2, 5));
        intervals.add((List<Interval>)interval.clone());
        interval.clear();

        interval.add(new Interval(9, 12));
        intervals.add((List<Interval>)interval.clone());
        interval.clear();

        EmployeeFreeTime et = new EmployeeFreeTime();
        System.out.println(et.employeeFreeTime(intervals));
    }

}
