package study;

public class algo09_22 {

	public static void main(String[] args) {
		String str = "samurai";
		String ending = "ra";
		System.out.println(str.substring(str.length()-ending.length(), str.length()));
		if(str.substring(str.length()-ending.length(), str.length()).contains(ending)) {
			System.out.println("포함");
		}
		else {
			System.out.println("미포함");
		}
	}

}
