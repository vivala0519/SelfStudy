package study;

import java.util.Arrays;

public class algo09_23 {

	public static void main(String[] args) {
		String s = "take me to semynak";
		String[] arr = s.split(" ");
		int[] sums = new int[arr.length];
		for(int i = 0; i < arr.length; i++) {
			int sum = 0;
			for(int j = 0; j < arr[i].length(); j++) {
				System.out.println(arr[i].charAt(j));
				System.out.println(arr[i].charAt(j) - 96);
				sum += arr[i].charAt(j) - 96;
				sums[i] = sum;
			}
		}
		System.out.println(Arrays.toString(sums));
		int max = sums[0];
		int maxIndex = 0;
		
		for(int i = 0; i < sums.length; i++) {
			if(sums[i] > max) {
				max = sums[i];
				maxIndex = i;
			}
		}
		System.out.println(max);
		System.out.println(maxIndex);
		System.out.println(arr[maxIndex]);
	}

}
