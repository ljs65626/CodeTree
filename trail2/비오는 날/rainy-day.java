import java.util.Scanner;

class Weather {
    String date, day, weather;

    public Weather(String date, String day, String weather) {
        this.date = date;
        this.day = day;
        this.weather = weather;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Weather[] w_list = new Weather[n];
        for (int i = 0; i < n; i++) {
            String date = sc.next();
            String day = sc.next();
            String weather = sc.next();
            w_list[i] = new Weather(date, day, weather);
            // Please write your code here.
        }

        int min_date = 9999;
        int min_index=0;
        for (int i = 0; i < n; i++) {
            if (w_list[i].weather.equals("Rain")) {
                if (Integer.parseInt(w_list[i].date.substring(0, 4)) < min_date) {
                    min_index = i;
                    min_date = Integer.parseInt(w_list[i].date.substring(0, 4));
                }
            }
        }

        System.out.print(w_list[min_index].date + " " + w_list[min_index].day + " " + w_list[min_index].weather);
    }
}