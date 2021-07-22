package study;

public class replaceDots {
	public static void main(String[] args) {
	String str = "one.two.three";
	String st = str.replaceAll("\\.", "-");
	System.out.println(st);
	}
}
