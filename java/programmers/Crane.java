import java.util.ArrayList;
class Solution1 {
    public static int solution(int[][] board, int[] moves) {
        ArrayList<Integer> basket = new ArrayList<>();
        int answer = 0;
        int[] memory = new int[board.length];
        int doll=0;
        for (int i=0; i<board.length;i++){
            for (int j=0; j<board.length;j++){
                System.out.printf("%d ", board[i][j]);
            }
            System.out.println();
        }
        
        for (int i=0; i<memory.length; i++){
            memory[i] = 31;
        }
        for(int move:moves){
            move--;
            System.out.println("move : "+move);
            doll = 0;
            if (memory[move]==31){
                for (int i=0; i<board.length;i++){
                    if (board[i][move]!=0){
                        doll = board[i][move];
                        board[i][move] = 0;
                        memory[move]=i+1;
                        break;
                    }
                }
            } else if(memory[move] <= board.length-1){
                doll = board[memory[move]][move];
                board[memory[move]][move] = 0;
                memory[move]++;
            }
            if (doll!=0) {
                if (basket.size()==0){
                    basket.add(doll);
                } else {
                    int predoll = basket.get(basket.size()-1);
                    basket.remove(basket.size()-1);
                    if (predoll!=doll){
                        basket.add(predoll);
                        basket.add(doll);
                    } else {
                        answer+=2;
                    }
                }
            }
            
            System.out.println("doll : "+doll+" answer : "+answer);
            System.out.println(basket);
            for (int i=0; i<board.length;i++){
                for (int j=0; j<board.length;j++){
                    System.out.printf("%d ", board[i][j]);
                }
                System.out.println();
            }
        }
        return answer;
    }
}

public class Crane {
    public static void main(String[] args){
        int[][] bo = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
        int[] mo = {1,5,3,5,1,2,1,4};
        System.out.println(Solution1.solution(bo, mo));
    }    
}