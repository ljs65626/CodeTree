import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    String name;
    int korean, english, math;

    public Student(String name, int korean, int english, int math) {
        this.name = name;
        this.korean = korean;
        this.english = english;
        this.math = math;
    }

    @Override
    public int compareTo(Student otherStudent) {
        if (this.korean==otherStudent.korean) {
            if (this.english==otherStudent.english) {
                return otherStudent.math - this.math;
            }
            else return otherStudent.english - this.english;
        }
        else return otherStudent.korean - this.korean;
    }

}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Student[] students = new Student[n];
        for (int i=0; i<n; i++) {
            String name = sc.next();
            int korean = sc.nextInt();
            int english = sc.nextInt();
            int math = sc.nextInt();
            students[i] = new Student(name, korean, english, math);
        }
        Arrays.sort(students);
        for (int i=0; i<n; i++) {
            System.out.println(students[i].name + " " + students[i].korean + " " + students[i].english + " " + students[i].math);
        }
    }
}