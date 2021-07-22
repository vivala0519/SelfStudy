package study;

import java.util.ArrayList;
import java.util.Arrays;

public class kata {

	public static void main(String[] args) {
		long n = 348597;
		int array = (int) n;
		String pow = String.valueOf(array);
		String transfor = pow.replaceAll("[^\\d]", "");
		int length = (int) (Math.log10(Integer.parseInt(transfor))+1);
		int rel[] = {0,0,0,0,0,0};
		System.out.println(length);
		System.out.println(transfor);
		
		String str = "";
		for(int i = 0; i<length; i++) {
				rel[length-i-1] = transfor.charAt(i)-48;
			}
		System.out.println(str);
		System.out.println(Arrays.toString(rel));
		
	}

}
