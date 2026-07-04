import java.util.Scanner;

class Promise {
    String code;
    char loc;
    int time;
    
    public Promise(String code, char loc, int time) {
        this.code = code;
        this.loc = loc;
        this.time = time;
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String code;
        char loc;
        int time;
        code = sc.next();
        loc = sc.next().charAt(0);
        time = sc.nextInt();
        Promise p = new Promise(code, loc, time);
        System.out.println("secret code : " + p.code);
        System.out.println("meeting point : " + p.loc);
        System.out.println("time : " + p.time);
    }
}