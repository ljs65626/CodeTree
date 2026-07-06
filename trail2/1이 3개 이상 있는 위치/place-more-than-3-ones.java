import java.util.Scanner;
public class Main {
    public static int n;

    public static int[] dxs = new int[]{1, 0, -1, 0};
    public static int[] dys = new int[]{0, 1, 0, -1};

    public static boolean in_range(int x, int y) {
        if (x>=0 && x<n && y>=0 && y<n) return true;
        else return false;
    }

    public static void main(String[] args) {
        // Please write your code here.
        int ans=0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[][] arr = new int[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                int nx=i;
                int ny=j;
                int cnt=0;
                for (int n_dir=0; n_dir<4; n_dir++) {
                    if (in_range(nx+dxs[n_dir], ny+dys[n_dir]) && arr[nx+dxs[n_dir]][ny+dys[n_dir]]==1) {
                        cnt+=1;
                    }
                }
                if (cnt>=3) ans+=1;
            }
        }
        System.out.print(ans);
    }
}
