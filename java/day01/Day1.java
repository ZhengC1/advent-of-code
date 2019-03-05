import java.io.*;
import java.util.*;

public class Day1 {

    public static void main(String[] args) throws Exception {
        part1();
        part2();
    }

    public static void part1() throws Exception {
        File file = new File("/home/chun/github/advent-of-code/java/day01/input.txt");
        Scanner scan = new Scanner(file);
        int sum = 0;
        while(scan.hasNextLine()) {
            sum += Integer.parseInt(scan.nextLine());
        }
        System.out.println(sum);
    }

    public static void part2() throws Exception {
        List<Integer> list = new ArrayList<Integer>();
        File file = new File("/home/chun/github/advent-of-code/java/day01/input.txt");
        Scanner scan = new Scanner(file);
        int sum = 0;
        Integer line;
        while(scan.hasNextLine()) {
            line = Integer.parseInt(scan.nextLine());
            list.add(line);
        }

        Set<Integer> hashSet = new HashSet<Integer>();
        int answer = 0;
        int index = 0;
        while (!hashSet.contains(answer)) {
           hashSet.add(answer);
           answer += list.get(index++ % list.size());
        }
        System.out.println(Integer.toString(answer));

    }
}
