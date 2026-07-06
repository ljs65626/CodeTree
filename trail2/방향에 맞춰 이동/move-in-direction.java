import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int[] dxs = new int[]{-1, 0, 1, 0};
        int[] dys = new int[]{0, -1, 0, 1};
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int nx, ny;
        nx=0;
        ny=0;
        for (int i = 0; i < n; i++) {
            char dir = sc.next().charAt(0);
            int dist = sc.nextInt();

            if (dir=='N') {
                nx+=(dxs[3]*dist);
                ny+=(dys[3]*dist);
            }
            else if (dir=='S') {
                nx+=(dxs[1]*dist);
                ny+=(dys[1]*dist);
            }
            else if (dir=='E') {
                nx+=(dxs[2]*dist);
                ny+=(dys[2]*dist);
            }
            else {
                nx+=(dxs[0]*dist);
                ny+=(dys[0]*dist);
            }
            // Please write your code here.
        }
        System.out.print(nx + " " + ny);
    }
}