package study;

import java.util.Arrays;

public class algo09_19 {
	public static void main(String[] args) {
		String s = "bitcoin take over the world maybe who knows perhaps";
		String[] arr = s.split(" ");
		int[] find_min = new int[arr.length];
		for(int i = 0; i < arr.length; i++) {
			find_min[i] = arr[i].length();
		}
		Arrays.sort(find_min);
		System.out.println(find_min[0]);
//		System.out.println(Arrays.toString(find_min));
//		System.out.println(Arrays.toString(arr));
	}
}
