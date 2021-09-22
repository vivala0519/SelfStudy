package study;

import java.util.Arrays;

public class algo09_21 {

	public static void main(String[] args) {
		String str = "Hello world !";
		String[] arr = str.split(" ");
		String result = "";
		System.out.println(arr[0].substring(0, 1));
		System.out.println(arr[0].substring(1));
		for(int i = 0; i < arr.length; i++) {
			if(!arr[i].matches("[^a-zA-Z0-9\\\\s]")) {
				arr[i] = arr[i].substring(1) + arr[i].substring(0, 1) + "ay";
			}
			result += arr[i];
			if(i < arr.length - 1) {
				result += " ";
			}
		}
		System.out.println(Arrays.toString(arr));
		System.out.println(result);
	}

}
