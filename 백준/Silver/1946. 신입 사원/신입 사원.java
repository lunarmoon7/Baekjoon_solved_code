import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = null;
    static StringBuilder sb = new StringBuilder();
    static StringBuffer sbf = new StringBuffer();

    public static void main(String[] args) throws Exception {
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            int cnt = 0;
            int minInterviewRank = Integer.MAX_VALUE;
            int N = Integer.parseInt(br.readLine());
            int score[][] = new int[N + 1][2];
            for(int j = 1; j <= N; j++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                score[j][0] = x;
                score[j][1] = y;
            }

            Arrays.sort(score, new Comparator<int []>() {
                @Override
                public int compare(int o1[], int o2[]){
                    return o1[0] - o2[0];
                }
            });

            for(int k = 1; k <= N; k++){
                if(score[k][1] < minInterviewRank){
                    cnt++;
                    minInterviewRank = score[k][1];
                }
            }

            System.out.println(cnt);

        }


    }
}
