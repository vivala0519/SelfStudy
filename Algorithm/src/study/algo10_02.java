package study;

import java.util.Arrays;

public class algo10_02 {

	public static void main(String[] args) {
		double[] arr = {0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
		double result = 0;
		for(int i = 0; i < arr.length; i++) {
			if(i == 0) {
				if(arr[i] != arr[i+1]) {
					if(arr[i+2] == arr[i+1]) {
						result = arr[i];
						System.out.println("case1:" + result);
						break;
					}
					else {
						result = arr[i+1];
						System.out.println("case2:" + result);
						break;
					}
				}
			}
			else {
				if(arr[i] != arr[i+1]) {
					result = arr[i+1];
					System.out.println("case3:" + result);
					break;
				}
			}
		}
		System.out.println(result);
	}

}
