package test;
public class Kata2 {
	public static int[] digitize(long n) {
		int array = (int) n;
		String trans = String.valueOf(array);
		String transfor = trans.replaceAll("[^\\d]", "");
		int length = (int)Math.log10(Integer.parseInt(transfor))+1;
		int[] digitize = new int[length];
		for(int i = 0; i<length; i++) {
			digitize[length-i-1] = transfor.charAt(i)-48;
		}
		return digitize;
	}
}