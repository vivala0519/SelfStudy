package study;

import java.util.Arrays;

public class Stringendswith {

	public static void main(String[] args) {
		String str = "sumo";
		String ending = "yumo";
		String[] s_arr = new String[str.length()];
		String[] end_arr = new String[ending.length()];

		for(int i = 0; i < str.length(); i++) {
			s_arr[i] = String.valueOf(str.charAt(i));
		}
		for(int i = 0; i < ending.length(); i++) {
			end_arr[i] = String.valueOf(ending.charAt(i));
		}
		int i = 1;
		String res = "";
		while(i <= ending.length()) {
			System.out.println(i);
			if(s_arr[s_arr.length-i].equals(end_arr[end_arr.length-i])) {
				System.out.println(s_arr[s_arr.length-i]);
				System.out.println(end_arr[end_arr.length-i]);
				i++;
				res =  "true";
			}
			else {
				res =  "false";
				break;
			}
		}
		System.out.println(res);
	}

}
