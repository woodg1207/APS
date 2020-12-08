class Solution1 {
    public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        int[] memory = new int[board[0].length];
        int doll;
        for (int i=0; i<memory.length; i++){
            memory[i] = 32;
        }

        for(int move:moves){
            if (memory[move]==32){
                for (int i=0; i<board.length;i++){
                    if (board[i][move]!=0){
                        doll = board[i][move];
                        memory[move]=i+1;
                    }
                }
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