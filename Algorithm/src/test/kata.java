package test;
public class kata {
	  public static int squareSum(int[] n) { 
		int sum = 0;
		int length = n.length;
		for(int i = 0; i<length; i++) {
			int res = 0;
			res = (int) Math.pow(n[i], 2);
			sum += res;
		}
		return sum;
	  }
}