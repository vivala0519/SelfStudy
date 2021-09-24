package study;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class algo09_24 {

	public static void main(String[] args) {
		String text = "";
		String[] arr = text.split(" ");
		System.out.println(Arrays.toString(arr));
		String result = "";
		try {
			for(int i = 0; i < arr.length; i++) {
				String word = "";
				String to_ascii = arr[i].substring(0, 1);
				byte[] bytes = to_ascii.getBytes(StandardCharsets.US_ASCII);
				System.out.println(bytes[0]);
				word += bytes[0];
				if(arr[i].length() == 2) {
					word += arr[i].substring(arr[i].length()-1, arr[i].length());
				}
				else if(arr[i].length() > 2) {
					word += arr[i].substring(arr[i].length()-1, arr[i].length());	
					word += arr[i].substring(2, arr[i].length()-1) + arr[i].substring(1, 2);
				}
				System.out.println(word);
				result += " " + word;
			}
			result = result.substring(1, result.length());
			System.out.println("result : " + result);
		
		} catch(Exception e){
			
		}
		
	}

}
