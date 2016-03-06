/**
 * GenEdMatcher
 *
 * Matches available courses to courses that satisfy degree requirements.
 *
 * @author Kevin Dong, dong70@purdue.edu, www.kevindong.net
 *
 * @version v1.0.0 (March 6, 2016; 4:15 PM ET)
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class GenEdMatcher {
    public static ArrayList<String[]> genEdCourses = new ArrayList<String[]>();
    public static ArrayList<String[]> inputtedCourses = new ArrayList<String[]>();
    public static ArrayList<String[]> matchingCourses = new ArrayList<String[]>();

    public void importCourses(String fileName, ArrayList<String[]> arrayList) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            String[] transition;
            while ((line = br.readLine()) != null) {
                transition = line.split("\t");
                arrayList.add(transition);
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        GenEdMatcher gem = new GenEdMatcher();
        if (args.length != 2) {
            System.out.println("Usage: \"java -jar GenEdMatcher.java [available_courses.txt] [GenEd_courses.txt]\"\n\nGenEdMatcher v1.0.0 (March 6, 2016; 4:15 PM ET)");
            return;
        }
        String list1 = args[0];
        String list2 = args[1];
        gem.importCourses(list1, inputtedCourses);
        gem.importCourses(list2, genEdCourses);
        for (int i = 0; i < inputtedCourses.size(); i++) {
            for (int j = 0; j < genEdCourses.size(); j++) {
                if (inputtedCourses.get(i)[0].equals(genEdCourses.get(j)[0])) {
                    if (matchingCourses.size() == 0) {
                        matchingCourses.add(inputtedCourses.get(i));
                    } else {
                        for (int k = 0; k < Math.max(matchingCourses.size(), 1); k++) {
                            if (matchingCourses.get(k)[0].equals(inputtedCourses.get(i)[0]) && matchingCourses.get(k)[1].equals(inputtedCourses.get(i)[1])) {
                                break;
                            } else if (k == matchingCourses.size() - 1) {
                                matchingCourses.add(inputtedCourses.get(i));
                            }
                        }
                    }

                }
            }
        }
        for (int i = 0; i < matchingCourses.size(); i++) {
            System.out.println(matchingCourses.get(i)[0] + " - " + matchingCourses.get(i)[1]);
        }
    }
}