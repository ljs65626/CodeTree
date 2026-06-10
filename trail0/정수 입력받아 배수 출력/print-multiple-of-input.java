import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=1; i<6; i+=1) {
            System.out.print((n*i) + " ");
        }
    }
}