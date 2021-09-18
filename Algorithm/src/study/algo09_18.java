package study;

import java.util.Arrays;

public class algo09_18 {

	public static void main(String[] args) {
		String s = "HelloWorld";
		int length = 2;
		if(s.length() % 2 != 0) {
			s += "_";
		}
		int num = s.length() / 2;
		String[] result = new String[num];
		int increase = 0;
		for(int i = 0; i < num; i++) {
			result[i] = s.substring(increase, length);
			length += 2;
			increase += 2;
		}
		System.out.println(Arrays.toString(result));
	}

}
