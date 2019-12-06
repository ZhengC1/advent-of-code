import java.io.*;
import java.util.*;

public class Day1 {

    private static List<String> list;

    public Day1() throws Exception {
        list = new ArrayList<String>();
        File file = new File("/home/chun/github/advent-of-code/java/day02/input.txt");
        Scanner scan = new Scanner(file);
        int sum = 0;
        String line;
        while(scan.hasNextLine()) {
            list.add(scan.nextLine());
        }
    }

    public static void main(String[] args)throws Exception {
        Day1 day = new Day1();
        day.part1();
    }

    public void part1() {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (String line : list) {
            Set<Integer> set = new HashSet<>();
            HashMap<Character, Integer> count = new HashMap<>();
            for (int i = 0; i < line.length(); i++) {
                Character key = line.charAt(i);
                Integer value = (count.get(key) == null) ?  0 : count.get(key);
                count.put(key, value + 1);
            }
            for (Integer i : count.values()) {
                if (i != 1) {
                    set.add(i);
                }
            }
            // { 1: 1, 2: 2, 3: 2 }
            for (Integer i : set) {
                Integer value = (map.get(i) == null) ?  0 : map.get(i);
                map.put(i, value + 1);
            }
        }
        Integer sum = 1;
        for (Integer i : map.values()) {
            sum = sum * i;
        }
        System.out.println(sum);
    }

    public void part2() {
    }
}
