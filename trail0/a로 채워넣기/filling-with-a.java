import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String text = sc.next();
        int leng = text.length();
        for (int i=0; i<leng; i++) {
            if (i==1) System.out.print("a");
            else if (i==leng-2) System.out.print("a");
            else System.out.print(text.charAt(i));
        }
    }
}