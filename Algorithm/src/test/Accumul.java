package test;

public class Accumul {
    
    public static String accum(String s) {
    	String result = carcul(s);
    	
    	return result;
    }
    
    public static String carcul(String str) {
		String res = "";
		for(int i = 1; i <= str.length(); i++) {
		// ���޹��� ���ڿ��� ���̵��� �ݺ�
			if(i != str.length()) {
			// �������ݺ� ������(������ �ݺ����� �ڿ� "-"�� ����� �ϱ� ����)
				for(int j = 0; j <= i-1; j++) {
				// 	���ڴ� ���ڼ�����ŭ �ݺ�
					if(j == 0) {
					// �� �ݺ��� ù ����
						if(i==1) {
						// �� ù ���ڴ� �ٷ� "-"�� �;� �ϱ⶧��
							res += String.valueOf(str.charAt(i-1)).toUpperCase() + "-";
						}
						else {
							res += String.valueOf(str.charAt(i-1)).toUpperCase();	
						}
					}
					else if(j==i-1) {
					// �� �ݺ��� ������ ����
						res += String.valueOf(str.charAt(i-1)).toLowerCase() + "-";
					}
					else {
						res += String.valueOf(str.charAt(i-1)).toLowerCase();
					}
				}
			}
			else {
			// ������ �ݺ�
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