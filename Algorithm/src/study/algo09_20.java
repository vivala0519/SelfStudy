package study;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class algo09_20 {

	public static void main(String[] args) {
		int[] ls = {0, 1, 3, 6, 10};
		List<Integer> arr = new ArrayList<>();
		int[] sums = new int[ls.length+1];
		for(int i = 0; i < ls.length; i++) {
			arr.add(i, ls[i]);
		}
		System.out.println(arr);
		int sum = Arrays.stream(ls).sum();
		sums[0] = sum;
		int length = arr.size();
		try {
		for(int i = 0; i < length; i++) {
			arr.remove(0);
			sum = 0;
			for (int number : arr) {
				sum += number;
			}
			sums[i+1] = sum;
			System.out.println(arr);
		}
		} catch(Exception e){
			
		}
		System.out.println(Arrays.toString(sums));
//		int sum = 0;
//		for(int i = 0; i < ls.length; i++) {
//			sum += ls[i];
//		}
//		int[] sums = new int[ls.length+1];
//		sums[0] = sum;
//		System.out.println(Arrays.toString(sums));
//		try {
//		for(int j = 0; j < ls.length; j++) {
//				for(int i = 0; i < ls.length; i++) {
//					if(i == ls.length - 1) {
//						ls[i] = 0;
//					}
//					else {
//						ls[i] = ls[i+1];
//					}
//				}
//			sum = 0;
//			for(int i = 0; i < ls.length; i++) {
//				sum += ls[i];
//			}
//			sums[j+1] = sum;
//			System.out.println(Arrays.toString(ls));
//		}
//		} catch(ArrayIndexOutOfBoundsException e){
//			
//		}
//
//		System.out.println(Arrays.toString(ls));
//		System.out.println(Arrays.toString(sums));
	}

}
