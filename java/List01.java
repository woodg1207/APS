import java.util.ArrayList;
public class List01 {
    public static void main(String[] args) {
        ArrayList<Integer> num = new ArrayList<Integer>();
        int i;
        for (i = 0; i<5; i++){
            num.add(i);
        }
        System.out.println(num);
        ArrayList<Integer> num10 = new ArrayList<Integer>(5);
        //용량 설정아님?
        for (i = 0; i <=10; i++){
            num10.add(i);
        }
        System.out.println(num10);
        //다른 반복문 python 같은 느낌
        int j = 0;
        for (int result: num10){
            
            if (result%2==0){
                System.out.println(num10.get(j));
            }
            j++;
        }
        
    }
}
