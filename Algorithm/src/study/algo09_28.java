package study;

public class algo09_28 {

	public static void main(String[] args) {
		String word = "testing";
		if(word.length() % 2 != 0) {
			System.out.println(word.charAt(word.length()/2));
			word = Character.toString(word.charAt(word.length()/2));
		}
		else {
			System.out.println(word.substring(word.length()/2 - 1, word.length()/2 + 1));
			word = word.substring(word.length()/2 - 1, word.length()/2 + 1);
		}
	}
}
