import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        int sum_val = a+b+c;
        int avg = (a+b+c)/3;
        System.out.println((a+b+c));
        System.out.println((a+b+c)/3);
        System.out.println(sum_val-avg);
    }
}