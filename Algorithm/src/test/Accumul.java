package test;

public class Accumul {
    
    public static String accum(String s) {
    	String result = carcul(s);
    	
    	return result;
    }
    
    public static String carcul(String str) {
		String res = "";
		for(int i = 1; i <= str.length(); i++) {
		// 전달받은 문자열의 길이동안 반복
			if(i != str.length()) {
			// 마지막반복 전까지(마지막 반복에는 뒤에 "-"가 없어야 하기 때문)
				for(int j = 0; j <= i-1; j++) {
				// 	글자당 글자순서만큼 반복
					if(j == 0) {
					// 각 반복의 첫 글자
						if(i==1) {
						// 맨 첫 글자는 바로 "-"가 와야 하기때문
							res += String.valueOf(str.charAt(i-1)).toUpperCase() + "-";
						}
						else {
							res += String.valueOf(str.charAt(i-1)).toUpperCase();	
						}
					}
					else if(j==i-1) {
					// 각 반복의 마지막 글자
						res += String.valueOf(str.charAt(i-1)).toLowerCase() + "-";
					}
					else {
						res += String.valueOf(str.charAt(i-1)).toLowerCase();
					}
				}
			}
			else {
			// 마지막 반복
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