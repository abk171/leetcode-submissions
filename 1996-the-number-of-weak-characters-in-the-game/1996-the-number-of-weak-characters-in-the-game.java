class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a, b) -> {
            if(a[0] == b[0])
                return a[1]-b[1];
            else
                return b[0]-a[0];
        });
        // for(int i = 0; i < properties.length; i++) {
        //     System.out.print("[");
        //     for(int j = 0; j < properties[0].length; j++) {
        //         System.out.printf("%d,", properties[i][j]);
        //     }
        //     System.out.println("]");
        // }
        int max = properties[0][1];
        int count = 0;
        for(int[] property : properties) {
            if(property[1] < max) count++;
            else max = property[1];
        }
        return count;
    }
}