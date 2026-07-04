import java.util.Scanner;

class Agent {
    char codename;
    int score;

    public Agent(char codename, int score) {
        this.codename = codename;
        this.score = score;
    }
}


public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        Agent[] a = new Agent[5];

        for (int i=0; i<5; i++) {
            char codename = sc.next().charAt(0);
            int score = sc.nextInt();
            a[i] = new Agent(codename, score);
        }

        int minResult = a[0].score;
        Agent minAgent = a[0];

        for (int i=1; i<5; i++) {
            if (a[i].score<minResult) {
                minResult = a[i].score;
                minAgent = a[i];
            }
        }

        System.out.print(minAgent.codename + " " + minAgent.score);
    }
}