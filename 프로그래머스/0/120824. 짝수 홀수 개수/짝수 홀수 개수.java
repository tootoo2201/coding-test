class Solution {
    public int[] solution(int[] num_list) {
        int evenCount = 0, oddCount = 0;
        for (int num : num_list) {
            if (num % 2 == 0) evenCount++; // 짝수 개수 증가
            else oddCount++; // 홀수 개수 증가
        }

        return new int[]{evenCount, oddCount}; 
    }
}
