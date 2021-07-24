package study;

public class Accumul {

	public static void main(String[] args) {
		String accum = "RqaEzty";
		String result = "";
		result = carcul(accum);
		System.out.println(result);
	}

	public static String carcul(String str) {
		String res = "";
		for(int i = 1; i <= str.length(); i++) {
			if(i != str.length()) {
				for(int j = 0; j <= i-1; j++) {
					if(j == 0) {
						if(i==1) {
							res += String.valueOf(str.charAt(i-1)).toUpperCase() + "-";
						}
						else {
							res += String.valueOf(str.charAt(i-1)).toUpperCase();	
						}
					}
					else if(j==i-1) {
						res += String.valueOf(str.charAt(i-1)).toLowerCase() + "-";
					}
					else {
						res += String.valueOf(str.charAt(i-1)).toLowerCase();
					}
				}
			}
			else {
				for(int j = 0; j <= i-1; j++) {
					if(j == 0) {
						res += String.valueOf(str.charAt(i-1)).toUpperCase();
					}
					else {
						res += String.valueOf(str.charAt(i-1)).toLowerCase();
					}
				}
			}
		}
		return res;
	}
}
