package study;

import java.util.Arrays;
import java.util.List;

public class algo09_17 {

	public static void main(String[] args) {
		String strng = "bsjq";
		List<String> a = Arrays.asList("bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs");

		for(int i=0; i<strng.length(); i++) {
			if(!a.contains(strng)) {
				System.out.println("false");
			}
			strng = strng.substring(1) + strng.charAt(0);
			System.out.println("true");
		}
	}

}
