import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> result = new ArrayList<> ();
        int sum;
        for (int i=0; i<numbers.length-1; i++){
            for (int j=i+1; j<numbers.length; j++){
                sum = numbers[i] + numbers[j];
                if (!result.contains(sum)){
                    result.add(sum);
                }
            }
        }
        Collections.sort(result);
        int[] r = new int[result.size()];
        for(int i=0; i<result.size(); i++){
            r[i] = result.get(i);
        }
        return r;
    }
}

public class TwoSum {
    public static void main(String[] args){
        int[] testcase = {5,0,2,7};
        // int[] testcase = 
        Solution tc = new Solution();
        System.out.println(tc.solution(testcase));
        for (int i:tc.solution(testcase)){
            System.out.printf("%d,",i);
        }
        System.out.println();
    }

}