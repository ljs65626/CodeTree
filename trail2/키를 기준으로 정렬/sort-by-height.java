import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    String name;
    int height, weight;

    public Student(String name, int height, int weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Student otherStudent) {
        return this.height - otherStudent.height;
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
            int height = sc.nextInt();
            int weight = sc.nextInt();
            students[i] = new Student(name, height, weight);
        }
        Arrays.sort(students);
        for (int i=0; i<n; i++) {
            System.out.println(students[i].name + " " + students[i].height + " " + students[i].weight);
        }
    }
}