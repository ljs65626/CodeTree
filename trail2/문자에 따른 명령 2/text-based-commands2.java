import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] dxs = new int[]{0, 1, 0, -1};
        int[] dys = new int[]{1, 0, -1, 0};
        int nx, ny, n_dir;
        nx=0;
        ny=0;
        n_dir=0;
        String inp = sc.next();

        for (int i=0; i<inp.length(); i++) {
            if (inp.charAt(i)=='F') {
                nx+=dxs[n_dir];
                ny+=dys[n_dir];
            }
            else if (inp.charAt(i)=='L') {
                n_dir = ((n_dir-1)+4)%4;
            }
            else {
                n_dir = (n_dir+1)%4;
            }
        }
        System.out.print(nx + " " + ny);
    }
}