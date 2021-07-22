package study;

public class squareSum {

	public static void main(String[] args) {
		int arr[] = {1,2,2};
		int sum = 0;
		int length = arr.length;
		for(int i = 0; i<length; i++) {
			int res = 0;
			res = (int) Math.pow(arr[i], 2);
			sum += res;
		}
		System.out.println(sum);
	}

}
